import pyexcel as p
import streamlit as st

def meetingPrep():
    #TODO: Add counters for tracking points

    book = p.get_book(file_name="Quotes.ods")
    return book.Meeting

def pomodoro(work_time,break_time):
    #TODO: with input work time, create button to begin work timer

    #TODO: with input break time, create button to begin break timer
    return

if __name__ == '__main__':
    print('Testing Work Mode...')
    meetingPrep()
