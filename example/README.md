# Dajngo Courier
App Django para fazer envio de notificações com plataformas diversas.

Por enquanto, só push notifications (via OneSignal) são suportadas. Envio de emails (com Mailgun) será o próximo a ser criado.

## Variáveis de ambiente
Este app demanda que as seguintes variáveis sejam declaradas no settings.py do projeto:
- COURIER_DEFAULT_PROVIDER
- COURIER_ONESIGNAL_APP_ID
- COURIER_ONESIGNAL_USER_ID
