init python:
    # Funzione per validare il nome
    def validate_name(name):
        name = name.strip()
        if len(name) < 2:
            return "Il nome deve contenere almeno 2 caratteri"
        if not name.isalpha():
            return "Usa solo lettere (no numeri o simboli)"
        return None


# Definizioni dei personaggi
define narrator = Character("Narratore", color="#ffffff")
define protagonist = Character("[player_name]", color="#00ff00")

# Variabile per il nome del giocatore
default player_name = "Misumi"

# Schermata per inserire il nome
screen name_input():
    modal True
    zorder 100
    
    # Variabile temporanea per l'input
    default temp_name = player_name
    default error_message = ""
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 75
        ypadding 75
        xsize 600
        
        vbox:
            spacing 25
            align (0.5, 0.5)
            
            text "Inserisci il tuo nome:":
                size 32
                xalign 0.5
                
            input:
                value ScreenVariableInputValue("temp_name")
                length 16
                xalign 0.5
                size 32
                allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567"
                
            if error_message:
                text "[error_message]":
                    color "#ff0000"
                    xalign 0.5
                
            hbox:
                xalign 0.5
                spacing 50
                
                textbutton "Conferma":
                    action [
                        If(
                            validate_name(temp_name) == None,
                            [
                                SetVariable("player_name", temp_name.strip()),
                                Return()
                            ],
                            SetScreenVariable("error_message", validate_name(temp_name))
                        )
                    ]
                
                textbutton "Annulla":
                    action Return()

