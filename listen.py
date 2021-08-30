# Write your code here :-)
import send
import make_plots
import read
import fbchat
from fbchat.models import *
from time import sleep

class bot(fbchat.Client):
    def onMessage(self,author_id,message_object,thread_id,thread_type,**kwargs):
        self.markAsDelivered(thread_id,message_object.uid)
        self.markAsRead(thread_id)
        
        #log.info('{} from {} in {}'.format(message_object,thread_id,thread_type.name))
        
        if author_id != self.uid:
            if message_object.text=='Plot':
                make_plots.make_and_send_plots(True)
            elif message_object.text=='Read':
                [t,h] = read.read(False)
                send.send_msg('Temp: {:.02f}*F Humidity: {:.01f}%'.format(t,h))
                sleep(2)
            else:
                send.send_msg('Try "Plot" for updated plots or "Read" for current reading')

if __name__=='__main__':
    sender_username = 'smartGeck@gmail.com'
    sender_password = '7373seal'
    client = bot(sender_username, sender_password)
    client.listen()