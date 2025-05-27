import pyautogui


def tirar_screenshot(caminho):
    screenshot = pyautogui.screenshot()
    screenshot.save(caminho)
    return caminho
