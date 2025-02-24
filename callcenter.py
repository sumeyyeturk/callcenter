import queue

class CallCenter:
    def __init__(self):
        self.queue=queue.Queue()
        
    def add_call(self,call_id,issue):
        print(f" {call_id}. Çağrı alınmıştır.")
        self.queue.put((call_id, issue))
        
    def call_isle(self):
        try:
            while not self.queue.empty():
                call_id,issue= self.queue.get()
                print(f"{call_id}. çağrı sıraya eklenmiştir.{issue}")
        except Exception as e:
            print(f"Beklenmedik hata oluştu: {e}")
            
call=CallCenter()
call.add_call(100,"Fatura sorgulama")
call.add_call(101,"Kalan internet kullanımı bilgileri")
call.add_call(102,"Modem kurulumu")
call.add_call(103,"İnternet bağlantı sorunu")

call.call_isle()
        
