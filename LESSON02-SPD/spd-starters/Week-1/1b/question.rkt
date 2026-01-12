;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname question) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #t)))
(require 2htdp/image)

;; Image Image -> Boolean
;; Given two images shape like rectangle, return true if First is larger than another

(check-expect (first-img-larger? (rectangle 10 20 "solid" "blue") (rectangle 20 20 "solid" "red")) false)
(check-expect (first-img-larger? (rectangle 10 20 "solid" "blue") (rectangle 10 20 "solid" "red")) false)
(check-expect (first-img-larger? (rectangle 10 20 "solid" "blue") (rectangle 10 10 "solid" "red")) true)



;(define (first-img-larger? img1 img2) true)
;
;(define (first-img-larger? img1 img2)
;  (... img1 img2))

(define (first-img-larger? img1 img2)
  (>
   (* (image-width img1) (image-height img1))
   (* (image-width img2) (image-height img2))
   )
  )