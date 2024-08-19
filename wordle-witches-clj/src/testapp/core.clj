(ns testapp.core
  (:gen-class)
  (:require
   [clojure.tools.logging :as logging]
   [ring.adapter.jetty :refer [run-jetty]]
   [bidi.ring :as bidi]
   [muuntaja.core :as m]
   [testapp.scraping :refer [create-csv]])
  (:import
   [java.util.logging Level]))

(defn- hello-handler [req]
  {:status 200
   :body {:message "hello"}})

(defn- hoge-handler [req]
  {:status 200
   :body {:message "hoge"}})

(defn- not-found-handler [_]
  {:status 404
   :body {:message "not found"}})

(defn- response-body-marshaller
  [handler]
  (fn [req]
    (let [{:as res :keys [body]} (handler req)
          res (assoc-in res [:headers "content-type"] "application/json")]
      (assoc-in res [:body] (m/encode "application/json" body)))))

(def handler
  (-> (bidi/make-handler
       ["/" {"hello" hello-handler
             "hoge" hoge-handler
             true not-found-handler}])
      (response-body-marshaller)))

(defn start-server []
  (logging/info "starting server on localhost:9000...")
  (run-jetty handler {:port 9000}))

(defn -main
  [& args]
  (let [cmd (first args)]
    (cond
      (= cmd "create-csv") (create-csv "witches.csv")
      :else (start-server))))
