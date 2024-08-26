(ns testapp.importcsv
  (:require
   [clojure.java.io :as io]
   [clojure.data.csv :as csv]))

(defn- columns []
  [:name :img :nation :branch :unit :team :birthday])

(defn- line->record [line]
  (zipmap (columns) line))

(defn- empty->nil [s]
  (if (empty? s) nil s))

(defn- empty-values->nil [record]
  (let [impl
        (fn self [r cols]
          (if (empty? cols)
            r
            (self
             (assoc-in r [(first cols)] (empty->nil (get r (first cols))))
             (rest cols))))]
    (impl record (columns))))

(defn import-csv [filename]
  (with-open [reader (io/reader filename)]
    (doall
     (->> (csv/read-csv reader)
          (map line->record)
          (map empty-values->nil)
          (map println)))))
