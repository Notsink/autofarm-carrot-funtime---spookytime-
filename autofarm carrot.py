import time
import threading
from pynput import mouse, keyboard

# Настройки
CLICK_DELAY = 0.1  # Задержка между кликами (в секундах)
RUNNING = False    # Флаг для управления циклом

mouse_controller = mouse.Controller()

def click_cycle():
    """Цикл: 4 ПКМ → 1 ЛКМ"""
    while RUNNING:
        for _ in range(4):
            if not RUNNING:
                return
            mouse_controller.click(mouse.Button.right)
            time.sleep(CLICK_DELAY)

        if not RUNNING:
            return
        mouse_controller.click(mouse.Button.left)
        time.sleep(CLICK_DELAY)

def on_press(key):
    global RUNNING
    if key == keyboard.Key.f6 and not RUNNING:
        RUNNING = True
        print("▶️ Запуск цикла...")
        threading.Thread(target=click_cycle, daemon=True).start()
    elif key == keyboard.Key.f7 and RUNNING:
        RUNNING = False
        print("⏸️ Цикл остановлен.")

def on_release(key):
    pass  # Можно использовать для дополнительной логики

# Запускаем слушатель клавиатуры
print("Нажми F6 для запуска, F7 для остановки. Ctrl+C для выхода.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        print("\nВыход.") 