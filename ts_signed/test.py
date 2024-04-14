from bs4 import BeautifulSoup
import requests

import pyaudio  
import wave  
import time

def play_alarm():
	#define stream chunk   
	chunk = 1024  
	  
	while True:
		#open a wav format music  
		f = wave.open('mixkit-alert-alarm-1005.wav',"rb")  
		#instantiate PyAudio  
		p = pyaudio.PyAudio()  
		#open stream  
		stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
		                channels = f.getnchannels(),  
		                rate = f.getframerate(),  
		                output = True)  
		#read data  
		data = f.readframes(chunk)  
		  
		#play stream  
		while data:  
		    stream.write(data)  
		    data = f.readframes(chunk)  
		  
		#stop stream  
		stream.stop_stream()  
		stream.close()  
		  
		#close PyAudio  
		p.terminate() 


if __name__ == '__main__':

	while True:
		time.sleep(5)
		print("looping")

		try:
			website_main = 'https://store.taylorswift.com/'
			res_main = requests.get(website_main).text
			soup_main = BeautifulSoup(res_main,'lxml')

			check_1 = "View Product" in [x.text for x in soup_main.find_all('a')]
			check_2 = "cart" in [(x.text.lower()) for x in soup_main.find_all('a')]

			if not check_1 or check_2:
				play_alarm()

			time.sleep(5)

			website_vinyl = "https://store.taylorswift.com/products/the-tortured-poets-department-vinyl-bonus-track-the-manuscript-with-hand-signed-photo"
			res_vinyl = requests.get(website_vinyl).text
			soup_vinyl = BeautifulSoup(res_vinyl,'lxml')
			check_vinyl = "Not Available" == [x.text.strip() for x in soup_vinyl.find_all("button") if len(x.text.strip()) > 0][0]

			website_cd = "https://store.taylorswift.com/products/the-tortured-poets-department-cd-bonus-track-the-manuscript-with-hand-signed-photo"
			res_cd = requests.get(website_cd).text
			soup_cd = BeautifulSoup(res_cd,'lxml')
			check_cd = "Not Available" == [x.text.strip() for x in soup_cd.find_all("button") if len(x.text.strip()) > 0][0]
			if not check_vinyl or not check_cd :
				play_alarm()

		except:
			print("Something Failed")
			play_alarm()