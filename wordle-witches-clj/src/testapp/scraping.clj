(ns testapp.scraping
  (:require
   [clj-http.client :as client]
   [net.cgrand.enlive-html :as html]
   [clojure.string :as string]
   [clojure.java.io :as io]
   [clojure.data.csv :as csv]))

(defn- fetch-table-records []
  (let [html-data (:body (client/get
                          "https://worldwitches.fandom.com/wiki/List_of_Witches"
                          {:cookie-policy :none}))]
    (-> html-data
        (html/html-snippet)
        (html/select [:table])
        (#(filter (fn [node] (= "wikitable sortable" (:class (:attrs node)))) %))
        (first)
        (html/select [:tr])
        (rest))))  ;; skip headers

(defn- trim [s]
  (when (some? s) (string/trim s)))

(defn- empty->nil [s]
  (if (= s "") nil s))

(defn- extract-name-and-img [td]
  (let [extract-name
        (fn [td]
          (-> td
              (html/select [:center])
              (first)
              (:content)
              (first)
              (:content)
              (first)
              (trim)
              (empty->nil)))
        extract-img
        (fn [td]
          (-> td
              (html/select [:img])
              (first)
              (:attrs)
              ((fn [attrs]
                 (let [s (:data-src attrs)]
                   (if (some? s)
                     s
                     (:src attrs)))))
              (trim)
              (empty->nil)))]
    {:name (extract-name td)
     :img (extract-img td)}))

(defn- extract-nation [td]
  (->
   td
   (html/select [:a])
   (rest) (first) ;; 2nd <a> contains the nation
   (:content)
   (first)
   (trim)
   (empty->nil)
   ((fn [x] {:nation x}))))

(defn- extract-branch [td]
  {:branch (empty->nil (trim (first (:content td))))})

(defn- extract-unit [td]
  {:unit (empty->nil (trim (first (:content td))))})

(defn- extract-team [td]
  {:team (empty->nil (trim (first (:content td))))})

(defn- extract-birthday [td]
  {:birthday (empty->nil (trim (first (:content td))))})

(defn- tr->record [tr]
  (->> tr
       (#(html/select % [:td]))
       (interleave [:name-and-img :nation :branch :unit :team :birthday])
       (partition 2) ;; (:a 1 :b 2) -> ((:a 1) (:b 2))
       (map (fn [[kind td]]
              (cond
                (= kind :name-and-img) (extract-name-and-img td)
                (= kind :nation) (extract-nation td)
                (= kind :branch) (extract-branch td)
                (= kind :unit) (extract-unit td)
                (= kind :team) (extract-team td)
                (= kind :birthday) (extract-birthday td))))
       (apply merge)))

(defn- columns []
  [:name :img :nation :branch :unit :team :birthday])

(defn- record->values [columns record]
  (map
   #(% record)
   (map (fn [c] #(c %)) columns)))

(defn- write-csv [filename records]
  (with-open [writer (io/writer filename)]
    (->> (columns)
         (map name)
         ((fn [xs] [xs]))
         (csv/write-csv writer))
    (->> records
         (map #(record->values (columns) %))
         (csv/write-csv writer))))

(defn create-csv [filename]
  (->>
   (map tr->record (fetch-table-records))
   (write-csv filename)))

