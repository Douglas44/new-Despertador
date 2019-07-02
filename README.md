# new-Despertador
""  Despertador com sistema de notificação na tela do usuário ""
Nesse projeto foi importador o módulo Win10toast que é responsável por enviar uma notificação
na tela do usuário quando o tempo chegar ao limite
Módulo: from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Sample Notification","Python is awesome!!!")
