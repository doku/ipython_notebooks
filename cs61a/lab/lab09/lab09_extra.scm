;; Extra Scheme Questions ;;

; Q5
(define (square x) (* x x))

(define (pow b n)
    (if (= 0 n)
        1
        (if (= (modulo n 2) 0)
            (square
                    (pow b (/ n 2))  
            )
            (* b 
               (square 
                       (pow b 
                            (/ (- n 1) 2 )
                        )
               ) 
            )
        )
    )
)

; Q6
(define lst
    (cons (cons 1 nil) (cons 2 (cons (cons 3 4) (cons 5 nil)) ))
)

; Q7
(define (composed f g)
    (lambda (x) 
          (f (g x))
    )
)

; Q8
(define (remove item lst)
    (filter (lambda (x) (not (= x item))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q9
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
    (if (= (min a b) 0)
        (max a b)
             (if (= (max a b) a)
                (if (not (= (modulo a b) 0))
                    (gcd b (modulo a b))
                    b
                )
                (gcd b a
                )
            )
        
    )
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q10
(define (no-repeats s)
    (if (or (= (length s) 1) (= (length s) 0)) 
        s
        (cons (car s) 
              (filter 
                   (lambda (x) 
                         (not (= x (car s)))
                   )
                   (no-repeats (cdr s))
              )
        )
    )
)

; Q11
(define (substitute s old new)
    (if (= (length s) 0)
        s
        (if (= (length s) 1)
             (if (= (car s) old)
                 (cons new nil)
                 (cons old nil)
             )
             (if (= (car s) old)
                (cons new (substitude (cdr s) old new))
                (cons old (substitude (cdr s) old new))
            )
         )
    )
)

; Q12
(define (sub-all s olds news)
  'YOUR-CODE-HERE
)