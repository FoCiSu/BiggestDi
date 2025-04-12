
# Inizio del gioco
label start:
    # Mostra la schermata per inserire il nome
    call screen name_input
    
    # Se il nome è vuoto, usa quello di default
    if not player_name.strip():
        $ player_name = "Misumi"
    
    # Inizio della storia
    scene bg_citta with fade
    narrator "Benvenuto nel gioco, [player_name]!"
    protagonist "Ehi, sono [player_name]! È un piacere conoscerti!"
    
    return