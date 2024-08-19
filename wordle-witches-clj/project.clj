(defproject testapp "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "EPL-2.0 OR GPL-2.0-or-later WITH Classpath-exception-2.0"
            :url "https://www.eclipse.org/legal/epl-2.0/"}
  :dependencies [[org.clojure/clojure "1.11.1"]
                 [org.clojure/tools.logging "1.3.0"]
                 [ring/ring-core "1.12.2"]
                 [ring/ring-jetty-adapter "1.8.2"]
                 [bidi "2.1.6"]
                 [metosin/muuntaja "0.6.10"]
                 [clj-http "3.13.0"]
                 [enlive "1.1.6"]
                 [org.clojure/data.csv "1.1.0"]]
  :main ^:skip-aot testapp.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all
                       :jvm-opts ["-Dclojure.compiler.direct-linking=true"]}})
