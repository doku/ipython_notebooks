(define (find s predicate)
    (if (null? s) 
        #f
        (if (predicate (car s))
            (car s)
            (find (cdr-stream s) predicate)
        )
    )
  )

(define (scale-stream s k)
    (if (null? s) 
      nil
      (cons-stream (* (car s) k) 
        (scale-stream (cdr-stream s) k)
      )
    )
  
)
(define (map-stream s pred)
    (if (null? s)
      nil
      (cons-stream (pred (car s)) (map-stream (cdr-stream s) pred))
    )
)
(define (any s)
    (if (null? s)
      #F
      (if (car s)
        #t
        (any (cdr-stream s))  
      )
    )
)

(define (has-cycle s)
  (define (in_list x s) 
        (if (null? s)
          False
          (if (eq? x (car s)) 
                True
                (in_list x (cdr s))
          )
        )
  )
  (define (helper seen s) 
        (if (null? s)
            False
            (if (in_list (car s) seen)
              True
              (helper (cons (car s) seen) (cdr-stream s)) 
            )
        )
  ) 
  (helper (list) s)
)
(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
