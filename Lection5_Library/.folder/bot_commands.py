from turtle import up
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *



def greeting_command(update: Update, context: CallbackContext):
    log(update,context)
    update.message.reply_text(f'Oh my dear {update.effective_user.first_name}')
    update.message.reply_text(f'Make your choice:\n/time - time right now\n/help - see all functions\n/sum - write two numbers with whitespace')

def help_command(update: Update, context: CallbackContext):
    log(update,context)
    update.message.reply_text(f'/start\n/time\n/help\n/sum')

def time_command(update: Update, context: CallbackContext):
    log(update,context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def get_firstNum(update: Update, context: CallbackContext):
    update.message.reply_text(f'Введите первое число:')
    num1 = update.message.text
    num1 = float(num1)

def get_secondNum(update: Update, context: CallbackContext):
    update.message.reply_text(f'Введите второе число:')
    num2 = update.message.text
    num2 = float(num2)
    
def sum_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Введите первое число:')
    num1 = update.message.text
    num1 = float(num1)
    update.message.reply_text(f'Введите второе число:')
    num2 = update.message.text
    num2 = float(num2)
    update.message.reply_text(f'{num1} + {num2} = {num1+num2}')

