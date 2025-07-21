import pika

def get_message(channel, queue_name):
    method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)
    if method_frame:
        return body.decode()
    return ""

def send_message(channel, queue_name, message):
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    while True:
        request = get_message(channel, "requests")
        if request:
            uuid, item, quantity = request.split(";")
            print("Solicitud recibida:")
            print(f"Mensaje no. {uuid}")
            print(f"Ítem: {item}")
            print(f"Cantidad: {quantity}")
            price = input("Ingrese su precio: ")

            message = f"{uuid};{price}"
            send_message(channel, "quotations", message)

        answer = get_message(channel, "answers")
        if answer:
            uuid, accepted = answer.split(";")
            print("Respuesta recibida:")
            print(f"Mensaje no. {uuid}")
            print(f"¿Cotización aceptada?: {accepted}")

if __name__ == "__main__":
    main()
