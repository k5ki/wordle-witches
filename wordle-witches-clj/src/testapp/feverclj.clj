(ns testapp.feverclj)

;; https://4clojure.oxal.org

;; Problem 22
(def my-count
  (fn [xs]
    (let [impl
          (fn impl'
            [xs' acc]
            (if (= (count xs') 0)
              acc
              (impl' (rest xs') (+ acc 1))))]
      (impl xs 0))))

;; Problem 23
(def my-reverse
  (fn [xs]
    (let [impl
          (fn impl'
            [xs' acc]
            (if (= (count xs') 0)
              acc
              (impl' (rest xs') (conj acc (first xs')))))]
      (impl xs '()))))

;; Problem 24
(def sum
  #(reduce + 0 %))

;; Problem 25
(def filter-odds
  #(filter odd? %))

;; Problem 26
(def fib
  (fn [n]
    (let [impl
          (fn impl'
            [acc a b n]
            (if (= n 0)
              (conj acc a b)
              (impl' (conj acc a) b (+ a b) (- n 1))))]
      (cond
        (= n 0) '()
        (= n 1) '(1)
        :else (seq (impl [] 1 1 (- n 2)))))))

;; Problem 27
(def palindrome?
  (fn [xs] true))
