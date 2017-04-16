(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.
(define (map proc items)
  (if (null? items) 
    nil
    (cons (proc (car items)) (map proc (cdr items)))
    )
)

(define (cons-all first rests)
    (define helper (lambda (x) (append (list first) x)))
  (map helper rests)
)
;;(define (cons-all first rests)
;    (if (null? rests)
;        nil
;        (cons (append first (car rest)) 
;            (cons-all first (cdr rest))
;        )
;    )
(define (zipper a b) (if (null? a) nil (cons (cons (car a) (cons (car b) nil)) (zipper (cdr a) (cdr b)) )))

(define (zip pairs)
    (define (first lst)
      (if (null? lst)
        '()
        (cons (car (car lst)) (first (cdr lst)))
      )
    )
    (define (second lst)
      (if (null? lst)
        '()
        (cons (car (cdr (car lst))) (second (cdr lst)))
      )
    )
  (list (first pairs) (second pairs))
  ;(cons (cons-all (car (car pairs)) (cdr pairs)) (cons-all (car (cdr (car pairs))) (cdr pairs)))     
)

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
    (define (helper x s)
        (if (null? s) 
            nil
            (cons (cons x (cons (car s) nil)) (helper (+ x 1) (cdr s)))
        )
    )
    (helper 0 s) 
  )
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 18
  (cond 
    ((= total 0) (cons nil nil))
    ((< total 0) '())
    ((null? denoms) '())                 
    (else (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms))
         (list-change total (cdr denoms) ))
    )
  )
; (if (= total 0) 
 ;       (car denoms)
 ;       (if (< total 0)
 ;            nil
 ;            (cons (list-change (- total (car denoms)) denoms )
 ;               (list-change total (cdr denoms))
 ;            )
 ;       )
 ;   )
  
  )
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
            expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
        (list 'quote (eval expr))
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (append (list form (map let-to-lambda params)) (map let-to-lambda body))
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr))
               (c (zip (cadr expr))))
           ; BEGIN PROBLEM 19
           
                (append (list (list 'lambda (map let-to-lambda (car c)) (let-to-lambda (car body)))) (map let-to-lambda (car (cdr c)))) 
                ;(append ((lambda (car c) body) (cdr c)))
            
           ;((lambda (car (zip values)) body) (map let-to-lambda (car (cdr (zip values)))))
          
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr)
         ; END PROBLEM 19
         )))
