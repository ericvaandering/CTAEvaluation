#! /usr/bin/env python3

import random

# We've just read the tape label. We are ready to read file 2 on the physical tape, file 1 according to Enstore

tape_position = 2
enstore_position = 1

def set_enstore_pos():
    global enstore_position
    global tape_position
    enstore_position = tape_position - 1


def read_file():
    global tape_position
    tape_position += 1
    set_enstore_pos()

def rewind():
    global tape_position
    tape_position = 1
    set_enstore_pos()

def spaceFileMarksForward(delta):
    global tape_position
    tape_position += delta
    set_enstore_pos()

def spaceFileMarksBackwards(delta):
    global tape_position
    tape_position -= delta
    set_enstore_pos()

def seek(f_seq):
    global tape_position
    fSeq_delta = f_seq - tape_position;

    if f_seq == 1 :
        rewind()
        spaceFileMarksForward(1)
    elif fSeq_delta == -1:
        pass # do nothing we are in the correct place
    elif fSeq_delta >= 0:
        spaceFileMarksForward(fSeq_delta+1)
    else: # fSeq_delta < 0
        spaceFileMarksBackwards(abs(fSeq_delta))
        spaceFileMarksForward(1)  # Read the file mark # m_session.m_drive.readFileMark("[EnstoreFileReader::position] Reading file mark right before the header of the file we want to read");

    print(f"Wanted to seek to {f_seq}. We are actually at {enstore_position} ({tape_position} on the tape)")
     # m_session.setCurrentFseq(fSeq);

files = [1,2,3,4, 10 , 12, 6]

for i in range(20):
    files.append(random.randint(20,1000))

for f_num in files:
    seek(f_num)
    read_file()
