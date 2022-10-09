from di import DI
from listeners import RabbitListener
from services import SkService
from signal import signal, SIGTERM, SIGINT


def main():
    listener = RabbitListener(SkService())
    listener.run()

    def handle_sigterm(*_):
        print("Shutdown signal received")
        listener.close()
        print("Shutdown gracefully")

    signal(SIGTERM, handle_sigterm)
    signal(SIGINT, handle_sigterm)
    try:
        listener.close()
    except KeyboardInterrupt:
        handle_sigterm()


if __name__ == '__main__':
    DI()
    main()
