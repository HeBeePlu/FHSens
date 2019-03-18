#
# Richtungserkennung Lucas-Kanade
#
# Hendrik Beecken
# 10.08.2018
#
#
# Code angepasst aus Open CV Beispiel
# https://docs.opencv.org/trunk/d7/d8b/tutorial_py_lucas_kanade.html


import numpy as np
import cv2 
from datetime import datetime
import time

#Liste für Stillstandserkennung mit 25 einträgen
laenge = 35
liste = list(range(laenge))
log = []

#Parameter zur Frameverkleinerung
shrinkX = 0.8
shrinkY = 0.8

#Liste zum Zählen der Richtungsangaben
zaehlerListe = [0,0,0,0]

#Auslöservariable bei Richtungswechsel
wechsel = 0

#Video von Webcam
cap = cv2.VideoCapture(0)

#Video von Festplatte (muss im selben Verzeichnis liegen wie dieses Script)
#cap = cv2.VideoCapture('dateiname')

# Parameter für Shi-Tomasi Feature Detektion
feature_params = dict( maxCorners = 15,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )
# Parameter für Lucas-Kanade Optical Flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
# Zufällige Farben erzeugen zur Darstellung der Features
color = np.random.randint(0,255,(100,3))
# Features im ersten Frame finden
ret, old_frame = cap.read()

#Frame verkleinern
old_frame_smaller= cv2.resize(old_frame, (0,0), fx= shrinkX, fy=shrinkY, interpolation = cv2.INTER_AREA)
old_gray = cv2.cvtColor(old_frame_smaller, cv2.COLOR_BGR2GRAY)
mask = np.zeros_like(old_frame_smaller)

#ohne verkleinern
#old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
#mask = np.zeros_like(old_frame)

p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

#Schleife um die Kameraposition zu prüfen. Messung starten mir Taste 'R'
print('Zum Start der Richtungserkennung drücke "R"')
while(1):
    ret, frame = cap.read()
    # Frame verkleinern
    frame_smaller = cv2.resize(frame, (0, 0), fx=shrinkX, fy=shrinkY, interpolation=cv2.INTER_AREA)
    cv2.imshow('frame_setup', frame_smaller)

    #ohne verkleinern
    #cv2.imshow('frame_setup', frame)

    start = cv2.waitKey(5)
    if start == 114:
        cv2.destroyWindow('frame_setup')
        break
startZeit = time.time()
while(1):
    ret,frame = cap.read()

    # Frame verkleinern
    frame_smaller = cv2.resize(frame, (0, 0), fx=shrinkX, fy=shrinkY, interpolation=cv2.INTER_AREA)
    frame_gray = cv2.cvtColor(frame_smaller, cv2.COLOR_BGR2GRAY)

    #ohne verkleinern
    #frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Berechnung des optischen Flusses
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    good_new = p1[st==1]
    good_old = p0[st==1]

    # Punkte markieren und Richtungsvektoren berechnen
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        #frame verkleinern
        frame_show = cv2.circle(frame_smaller,(a,b),5,color[i].tolist(),-1)

        #ohne verkleinern
        #frame_show = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)

        #Vektor berechnen von alter zur neuer Position für alle Punkte in p0 und p1
        x = c - a
        y = d - b

        #Unterscheidung in welche Richtung der Vektor zeigt
        if abs(x) < abs(y) and y > 0:
            # print('hinten')
            liste.insert(0,'hinten')
        elif abs(x) < abs(y) and y < 0:
            # print('vorne')
            liste.insert(0, 'vorne')
        elif abs(x) > abs(y) and x < 0:
            # print('links')
            liste.insert(0, 'links')
        elif abs(x) > abs(y) and x > 0:
            # print('rechts')
            liste.insert(0, 'rechts')

        #Löschen des letzten Eintrages um überlaufen der Liste zu verhindern
        del liste[-1]

    #zählen der letzten Einträge und Ausgabe des meist vorkommenden Wertes um Rauschen zu unterdrücken

    zaehlerListe[0] = liste.count('hinten')
    zaehlerListe[1] = liste.count('vorne')
    zaehlerListe[2] = liste.count('links')
    zaehlerListe[3] = liste.count('rechts')

    if zaehlerListe.index(max(zaehlerListe)) == 0 :
         print ('hinten')
         endZeit = time.time()
         dauer = endZeit - startZeit
         log.append(dauer)
         log.append('hinten')
         startZeit = time.time()
         wechsel = 1
    elif zaehlerListe.index(max(zaehlerListe)) == 1 :
        print ('vorne')
        endZeit = time.time()
        dauer = endZeit - startZeit
        log.append(dauer)
        log.append('vorne')
        startZeit = time.time()
        wechsel = 2
    elif zaehlerListe.index(max(zaehlerListe)) == 2 :
        print ('links')
        endZeit = time.time()
        dauer = endZeit - startZeit
        log.append(dauer)
        log.append('links')
        startZeit = time.time()
        wechsel = 3
    elif zaehlerListe.index(max(zaehlerListe)) == 3 :
        print('rechts')
        endZeit = time.time()
        dauer = endZeit - startZeit
        log.append(dauer)
        log.append('rechts')
        startZeit = time.time()
        wechsel = 4

    img = cv2.add(frame_show,mask)
    cv2.imshow('frame',img)

    # Aktualisieren der alten Features im alten Frame für neuen Durchlauf
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)

    # wenn zu wenig markante Punkte vorhanden sind, finde neue
    if len(p0) < 7:
        ret, old_frame = cap.read()

        # Frame verkleinern
        old_frame_smaller = cv2.resize(old_frame, (0, 0), fx=shrinkX, fy=shrinkY, interpolation=cv2.INTER_AREA)
        old_gray = cv2.cvtColor(old_frame_smaller, cv2.COLOR_BGR2GRAY)

        #ohne verkleinern
        #old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

        p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

    k = cv2.waitKey(5) & 0xff
    if k == 27:
        endZeit = time.time()
        dauerEnd = endZeit - startZeit

        # Datei für Datalogging erzeugen
        logfile = open('Log.txt', 'w')

        logLaenge = len(log)/2 - 1
        logfile.write(str(log[0]) + '\n')

        for i in range(int(logLaenge)):

            logfile.write(log[2*i+1] + ' ' + str((log[2*i+2])) + '\n')


        logfile.write(str(dauer))


        break

cv2.destroyAllWindows()
cap.release()