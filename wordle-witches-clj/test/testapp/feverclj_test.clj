(ns testapp.feverclj-test
  #_{:clj-kondo/ignore [:refer-all]}
  (:require
   [clojure.test :refer :all]
   [testapp.feverclj :refer :all]))

(deftest prob22
  (testing "count a sequence"
    (is (= (my-count '(1 2 3 3 1)) 5))
    (is (= (my-count "Hello World") 11))
    (is (= (my-count [[1 2] [3 4] [5 6]]) 3))
    (is (= (my-count '(13)) 1))
    (is (= (my-count '(:a :b :c)) 3))))

(deftest prob23
  (testing "reverse a sequence"
    (is (= (my-reverse [1 2 3 4 5]) [5 4 3 2 1]))
    (is (= (my-reverse (sorted-set 5 7 2 7)) '(7 5 2)))
    (is (= (my-reverse [[1 2] [3 4] [5 6]]) [[5 6] [3 4] [1 2]]))))

(deftest prob24
  (testing "sum it all up"
    (is (= (sum [1 2 3]) 6))
    (is (= (sum (list 0 -2 5 5)) 8))
    (is (= (sum #{4 2 1}) 7))
    (is (= (sum '(0 0 -1)) -1))
    (is (= (sum '(1 10 3)) 14))))

(deftest prob25
  (testing "find the odd numbers"
    (is (= (filter-odds #{1 2 3 4 5}) '(1 3 5)))
    (is (= (filter-odds [4 2 1 6]) '(1)))
    (is (= (filter-odds [2 2 4 6]) '()))
    (is (= (filter-odds [1 1 1 3]) '(1 1 1 3)))))

(deftest prob26
  (testing "fibonacci"
    (is (= (fib 3) '(1 1 2)))
    (is (= (fib 6) '(1 1 2 3 5 8)))
    (is (= (fib 8) '(1 1 2 3 5 8 13 21)))))

(deftest prob27
  (testing "palindrome detector"
    (is (= (palindrome? '(1 2 3 4 5)) false))
    (is (= (palindrome? "racecar") true))
    (is (= (palindrome? [:foo :bar :foo]) true))
    (is (= (palindrome? '(1 1 3 3 1 1)) true))
    (is (= (palindrome? '(:a :b :c)) false))))