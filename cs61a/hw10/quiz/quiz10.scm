(define (how-many-dots s)
    (if (list? s) 
        0
        (if (null? (cdr s))
            0
            (if (pair? (car s))
                (if (number? (cdr s))
                    (+ (how-many-dots (car s)) 1)
                    (+ (how-many-dots (car s)) (how-many-dots (cdr s)))
                )
                (if (number? (cdr s))
                    1
                    (how-many-dots (cdr s))
                )
            )
        )
    )
)

;;; Tests

(how-many-dots '(1 2 3))
; expect 0
(how-many-dots '(1 2 . 3))
; expect 1
(how-many-dots '((1 . 2) 3 . 4))
; expect 2
(how-many-dots '((((((1 . 2) . 3) . 4) . 5) . 6) . 7))
; expect 6
(how-many-dots '(1 . (2 . (3 . (4 . (5 . (6 . (7)))))))
; expect 0
