;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname space-invaders-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/universe)
(require 2htdp/image)

;; Space Invaders


;; Constants:

(define WIDTH  300)
(define HEIGHT 500)

(define INVADER-X-SPEED 1.5)  ;speeds (not velocities) in pixels per tick
(define INVADER-Y-SPEED 1.5)
(define TANK-SPEED 2)
(define MISSILE-SPEED 10)

(define HIT-RANGE 10)

(define INVADE-RATE 100)

(define BACKGROUND (empty-scene WIDTH HEIGHT))

(define INVADER
  (overlay/xy (ellipse 10 15 "outline" "blue")              ;cockpit cover
              -5 6
              (ellipse 20 10 "solid"   "blue")))            ;saucer

(define TANK
  (overlay/xy (overlay (ellipse 28 8 "solid" "black")       ;tread center
                       (ellipse 30 10 "solid" "green"))     ;tread outline
              5 -14
              (above (rectangle 5 10 "solid" "black")       ;gun
                     (rectangle 20 10 "solid" "black"))))   ;main body

(define TANK-HEIGHT/2 (/ (image-height TANK) 2))
(define TANK-Y (- HEIGHT TANK-HEIGHT/2))

(define MISSILE (ellipse 5 15 "solid" "red"))

(define BASE-DX 1)

;; Data Definitions:

(define-struct game (invaders missiles tank))
;; Game is (make-game  (listof Invader) (listof Missile) Tank)
;; interp. the current state of a space invaders game
;;         with the current invaders, missiles and tank position

;; Game constants defined below Missile data definition

#;
(define (fn-for-game s)
  (... (fn-for-loinvader (game-invaders s))
       (fn-for-lom (game-missiles s))
       (fn-for-tank (game-tank s))))



(define-struct tank (x dir))
;; Tank is (make-tank Number Integer[-1, 1])
;; interp. the tank location is x, HEIGHT - TANK-HEIGHT/2 in screen coordinates
;;         the tank moves TANK-SPEED pixels per clock tick left if dir -1, right if dir 1

(define T0 (make-tank (/ WIDTH 2) 1))   ;center going right
(define T1 (make-tank 50 1))            ;going right
(define T2 (make-tank 50 -1))           ;going left

#;
(define (fn-for-tank t)
  (... (tank-x t) (tank-dir t)))



(define-struct invader (x y dx))
;; Invader is (make-invader Number Number Number)
;; interp. the invader is at (x, y) in screen coordinates
;;         the invader along x by dx pixels per clock tick

(define I0 (make-invader 150 100 12))           ;not landed, moving right
(define I1 (make-invader 300 200 12)) 
(define I2 (make-invader 150 HEIGHT -10))       ;exactly landed, moving left
(define I3 (make-invader 150 (+ HEIGHT 10) 10)) ;> landed, moving right


#;
(define (fn-for-invader invader)
  (... (invader-x invader) (invader-y invader) (invader-dx invader)))


(define-struct missile (x y))
;; Missile is (make-missile Number Number)
;; interp. the missile's location is x y in screen coordinates

(define M1 (make-missile 150 300))                       ;not hit I1
(define M2 (make-missile (invader-x I1) (+ (invader-y I1) 10)))  ;exactly hit I1
(define M3 (make-missile (invader-x I1) (+ (invader-y I1)  5)))  ;> hit I1

#;
(define (fn-for-missile m)
  (... (missile-x m) (missile-y m)))



(define G0 (make-game empty empty T0))
(define G1 (make-game (list I0) (list M1) T1))
(define G2 (make-game (list I0 I1) (list M1 M2) T1))
(define G3 (make-game (list I1 I2) (list M1 M2) T1))


;; =================
;; Functions:

;; Game -> Game
;; start the world with (main G0)
;; 
(define (main g)
  (big-bang g                   ; Game
    (on-tick   next-state)     ; Game -> Game
    (to-draw   render)   ; Game -> Image
    (on-key    handle-key) ; Game KeyEvent -> Game
    (stop-when hit-bottom?)))     ; Game -> Boolean

;; Game -> Game
;; produce the next game state: tank invader missile
;; if missile y - invader y <= HIT-RANGE, invader will disappear
;; if missile hit the left or right edge, change the dx -> -dx
(check-expect (next-state (make-game empty empty T0)) (make-game empty empty (make-tank (+ (tank-x T0) (* (tank-dir T0) TANK-SPEED)) (tank-dir T0))))
(check-expect (next-state (make-game
                           (list (make-invader 150 100 12)
                                 (make-invader 150 188 12))
                           (list (make-missile 150 300)
                                 (make-missile 150 210))
                           T1))
              (make-game  
               (list (make-invader (+ 150 12) (+ 100 (* 12 (/ INVADER-Y-SPEED INVADER-X-SPEED))) 12))
               (list (make-missile 150 (- 300 MISSILE-SPEED)))
               (make-tank (+ (tank-x T1) (* (tank-dir T1) TANK-SPEED)) (tank-dir T1))))
; (define (next-state g) g)
(define (next-state g)
  (filter-hit-invader (next-game g)))

;  Game -> Game
; produce the next game state: tank invader missile
(check-expect (next-game G0) (make-game empty empty (make-tank (+ (tank-x T0) (* (tank-dir T0) TANK-SPEED)) (tank-dir T0))))
(check-expect (next-game G2) (make-game  
                              (list (make-invader (+ 150 12) (+ 100 (* 12 (/ INVADER-Y-SPEED INVADER-X-SPEED))) 12)
                                    (make-invader 300 (+ 200 (* 12 (/ INVADER-Y-SPEED INVADER-X-SPEED))) -12))
                              (list (make-missile 150 (- 300 MISSILE-SPEED))
                                    (make-missile (invader-x I1) (- (+ (invader-y I1) 10) MISSILE-SPEED)))
                              (make-tank (+ (tank-x T1) (* (tank-dir T1) TANK-SPEED)) (tank-dir T1))))
;(define (next-game g) g)
(define (next-game s)
  (make-game (random-add-invader (next-loinvader (game-invaders s)))
             (next-lom (game-missiles s))
             (next-tank (game-tank s))))

(define (random-add-invader loi)
  (cond [(> (random 100) INVADE-RATE) loi]
         [else (cons (make-invader (+ (/ WIDTH 5) (random (- WIDTH (/ WIDTH 2.5)))) 0 (randomPlusMinus BASE-DX)) loi)]
         ))

;; randomy produce a negative or positive version of the given number
(define (randomPlusMinus n)
  (cond [(= (random 2) 1) n]
        [else (- n)])
  )

;; ListOfInvader -> ListOfInvader
;; produce next invagers, x add dx, y add (* abs(dx) (/ INVADER-Y-SPEED INVADER-X-SPEED))
;; if (x+dx >= WIDTH) or (x+dx <= 0), dx = -dx
(check-expect (next-loinvader empty) empty)
(check-expect (next-loinvader (list I0)) (list (make-invader (+ 150 12) (+ 100 (* 12 (/ INVADER-Y-SPEED INVADER-X-SPEED))) 12)))
(check-expect (next-loinvader (list I0 I1)) (list
                                             (make-invader (+ 150 12) (+ 100 (* 12 (/ INVADER-Y-SPEED INVADER-X-SPEED))) 12)
                                             (make-invader 300 (+ 200 (* 12 (/ INVADER-Y-SPEED INVADER-X-SPEED))) -12)))
; (define (next-loinvader loi) loi)
(define (next-loinvader loi)
  (cond [(empty? loi) empty]
        [else
         (if (or
              (>= (+ (invader-x (first loi)) (invader-dx (first loi))) WIDTH)
              (<= (+ (invader-x (first loi)) (invader-dx (first loi))) 0))
             (cons (make-invader (invader-x (first loi))
                                 (+ (invader-y (first loi)) (* (abs(invader-dx (first loi))) (/ INVADER-Y-SPEED INVADER-X-SPEED)))
                                 (- (invader-dx (first loi))))
                   (next-loinvader (rest loi)))
             (cons (make-invader (+ (invader-x (first loi)) (invader-dx (first loi)))
                                 (+ (invader-y (first loi)) (* (abs(invader-dx (first loi))) (/ INVADER-Y-SPEED INVADER-X-SPEED)))
                                 (invader-dx (first loi)))
                   (next-loinvader (rest loi)))
             )]))

;; ListOfMissile -> ListOfMissile
;; next missiles: each y - MISSILE-SPEED
;; if missile <= 0 , clear the missile
(check-expect (next-lom empty) empty)
(check-expect (next-lom (list (make-missile 150 300) (make-missile 200 100)))
              (list (make-missile 150 (- 300 MISSILE-SPEED)) (make-missile 200 (- 100 MISSILE-SPEED))))
(check-expect (next-lom (list (make-missile 150 300) (make-missile 200 1)))
              (list (make-missile 150 (- 300 MISSILE-SPEED))))
;(define (next-lom lom) lom)
(define (next-lom lom)
  (cond [(empty? lom) empty]
        [else
         (if (<= (- (missile-y (first lom)) MISSILE-SPEED) 0)
             (next-lom (rest lom))
             (cons (make-missile (missile-x (first lom)) (- (missile-y (first lom)) MISSILE-SPEED)) (next-lom (rest lom))))]))

;; Game -> Game
;; clear the missile and invader when missile hited the invader: (<= -10 (- m-y i-y) 10)
(check-expect (filter-hit-invader G1) G1)
(check-expect (filter-hit-invader G2) (make-game (list I0) (list M1) T1))
(check-expect (filter-hit-invader (make-game (list I0 I1) (list M1 M3) T1)) (make-game (list I0) (list M1) T1))
;(define (filter-hit-invader g) g)
(define (filter-hit-invader g)
  (make-game
   (filter-invader (game-missiles g) (game-invaders g))
   (filter-missile (game-missiles g) (game-invaders g))
   (game-tank g)))

;; ListOfInvader Missile -> ListOfInvader
;; filter list of invaders, clear hitted
(check-expect (hit-invader (list I0) M1) (list I0))
(check-expect (hit-invader (list I0 I1) M2) (list I0))
(define (hit-invader loi m)
  (cond [(empty? loi) empty]
        [else
         (if (hit? (first loi) m)
             (hit-invader (rest loi) m)
             (cons (first loi) (hit-invader (rest loi) m)))]))

;; ListOfMissile ListOfInvader -> ListOfInvader
(define (filter-invader lom loi)
  (cond [(empty? lom) loi]
        [else
         (filter-invader (rest lom) (hit-invader loi (first lom)))]))

;; ListOfMissile Invader -> ListOfMissile
(define (hit-missile lom i)
  (cond [(empty? lom) empty]
        [else
         (if (hit? i (first lom))
             (hit-missile (rest lom) i)
             (cons (first lom) (hit-missile (rest lom) i)))]))

;; ListOfMissile ListOfInvader -> ListOfMissile
(define (filter-missile lom loi)
  (cond [(empty? loi) lom]
        [else
         (filter-missile (hit-missile lom (first loi)) (rest loi))]))

;; Invader Missile -> Boolean
(define (hit? i m)
  (and (= (missile-x m) (invader-x i)) (<= -10 (- (missile-y m) (invader-y i)) 10)))

(define (next-tank t)
  (cond [(<= (+ (tank-x t) (* (tank-dir t) TANK-SPEED)) 0) (make-tank 0 1)]
        [(>= (+ (tank-x t) (* (tank-dir t) TANK-SPEED)) WIDTH) (make-tank WIDTH -1)]
        [else (make-tank (+ (tank-x t) (* (tank-dir t) TANK-SPEED)) (tank-dir t))]))

;; Game -> Image
;; render the game 
(check-expect (render (make-game empty empty T0)) (place-image
                                                   TANK
                                                   (tank-x T0) TANK-Y
                                                   BACKGROUND))
(check-expect (render (make-game (list (make-invader 150 100 12)
                                       (make-invader 150 188 12))
                                 (list (make-missile 150 300)
                                       (make-missile 150 210))
                                 T1))
              (place-image
               INVADER
               150 100
               (place-image
                INVADER
                150 188
                (place-image
                 MISSILE
                 150 300
                 (place-image
                  MISSILE
                  150 210
                  (place-image
                   TANK
                   (tank-x T1) TANK-Y
                   BACKGROUND)))
                ))) 
;(define (render g) BACKGROUND)
(define (render s)
  (render-loinvader
   (game-invaders s)
   (render-lom
    (game-missiles s)
    (render-tank (game-tank s)))
   ))

(define (render-tank t)
  (place-image
   TANK
   (tank-x t) TANK-Y
   BACKGROUND))

(define (render-lom lom b)
  (cond [(empty? lom) b]
        [else
         (place-image
          MISSILE
          (missile-x (first lom)) (missile-y (first lom))
          (render-lom (rest lom) b))]))

(define (render-loinvader loi b)
  (cond [(empty? loi) b]
        [else
         (place-image
          INVADER
          (invader-x (first loi)) (invader-y (first loi))
          (render-loinvader (rest loi) b))]))

;; Game KeyEvent -> Game
;; handle the keys:
;;  produce missile at x,y of tank when press space;
;;  change the dir to -1 when press left
;;  change the dir to 1 when press right
(check-expect (handle-key (make-game empty empty T0) " ") (make-game empty (list (make-missile (tank-x T0) TANK-Y)) T0))
(check-expect (handle-key (make-game empty empty T0) "left") (make-game empty empty (make-tank (tank-x T0) -1)))
(check-expect (handle-key (make-game empty empty T0) "right") (make-game empty empty (make-tank (tank-x T0) 1)))
; (define (handle-key g ke) g)
(define (handle-key g ke)
  (cond [(key=? ke " ") (make-game (game-invaders g) (cons (make-missile (tank-x (game-tank g)) TANK-Y) (game-missiles g)) (game-tank g))]
        [(key=? ke "left") (make-game (game-invaders g) (game-missiles g) (make-tank (tank-x (game-tank g)) -1))]
        [(key=? ke "right") (make-game (game-invaders g) (game-missiles g) (make-tank (tank-x (game-tank g)) 1))]
        [else g]))

;; Game -> Boolean
;; if y = height( reach the bootom), stop game
;(define (hit-bottom? g) false)
(define (hit-bottom? g)
  (cond [(empty? (game-invaders g)) false]
        [else
         (or (>= (invader-y (first (game-invaders g))) HEIGHT) (hit-bottom? (make-game (rest (game-invaders g)) (game-missiles g) (game-tank g))))]))