# Guión del juego.

# Tamaño de la pantalla.
define width  = 1280
define height = 720


# Personajes principales.
# Don Nacho
define color_nombre_narco = "#FF8200"
define anon_n = Character("???", color=color_nombre_narco)
define narco = Character("Don Nacho", color=color_nombre_narco) # Ignacio Villanueva Alcallaga

# Los demás.
define empresario = Character("Harrison", color="#5599ff") # Robert Bobby harrison
define waton = Character("Jimeno") # Jimeno Montoya
define mecanica = Character("Lili") # Liliana Oliviera

# Personajes secundarios.
define guardia_1 = Character("Guardia 1", color="#584f63")
define guardia_2 = Character("Guardia 2", color="#aaa")
define guardia_3 = Character("Guardia 3", color="#a52c2b")
define guardia_4 = Character("Guardia 4", color="#a7a223")
define naufrago = Character("Naufrago", color="#5599ff")

# Escala de las imágenes.
image bg guard_1 = im.Scale('bg guard_1.png', width, height)
image bg guard_2 = im.Scale('bg guard_2.png', width, height)
image bg guard_3 = im.Scale('bg guard_3.png', width, height)
image bg guard_4 = im.Scale('bg guard_4.png', width, height)
image bg prison = im.Scale('bg prison.jpg', width, height)
image bg norte_sur = im.Scale('bg norte_sur.png', width, height)
image bg zombies = im.Scale('bg zombies.jpg', width, height)
image bg boat = im.Scale('bg boat.jpg', width, height)
#image fugitive one = im.Scale('fugitive one.png', width, height)


# Textos del narrador & el contexto.
define texto_centrado = Character(None, what_xalign=0.5, what_text_align=0.5, text_xpos=0.5, window_yalign=0.5)
define contexto = Character(None, what_xalign=0.5, what_text_align=0.5, text_xpos=0.5, window_yalign=0.5, what_color="#e79600")

# Helpers
#texto_centrado "{i}{/i}"

# Se inicia el juego.
label start:

    # Detener la música del menú principal.
    stop music fadeout 2.0

    # Al inicio el fondo es de color negro.

    # Fondo prisión.
    scene bg prison

    # Hablado por narrador, centrado en el eje X e Y.
    texto_centrado "{i}Prisión de Guantanamo, Cuba{/i}"

    # Personajes secundarios comienzan el diálogo.
    scene bg guard_1
    guardia_1 "¡Los infectados están entrando por el muro este!"
    scene bg guard_2
    guardia_2 "¡Invadieron la zona norte, el muro practicamente ya no existe!"
    scene bg guard_3
    guardia_3 "¡Estamos teniendo una fuga de reclusos en la zona sur!"
    scene bg guard_4
    guardia_4 "Acaban de confirmar que {b}ÉL{/b} esta entre los que se han fugado."

    # Fondo inicial.
    scene bg forest

    # Aparece uno de los protagonistas.
    show fugitive one:
        ease .5 zoom 1.5 xoffset 500 yoffset 50
        #moves right 100px, bottom 50px.
        #set to 0 when you return later.

    # Personaje principal inicia su diálogo.
    anon_n "¡Finalmente, después de 6 años, soy libre!"
    anon_n "¡Había estado esperando por este momento!"

    contexto "Contexto: \n{i}Observando a lo lejos{/i}"

    anon_n "¡Dios, ya sabía acerca de esto, pero verlo en persona va más allá de mi imaginación!"

    scene bg zombies
    contexto "Contexto: \n{i}Se acerca una horda de infectados{/i}"
    scene bg norte_sur
    menu:
        "¿Hacia dónde debería correr?"
        "Correr hacia el norte":
            jump ir_al_norte
        "Correr hacia el sur":
            jump ir_al_sur

    label ir_al_norte:
        # Bad ending
        texto_centrado "{i}Los guardias suponían que escaparía por el norte{/i}"
        extend "{p}{i}No logró llegar muy lejos y quedó rodeado de guardias{/i}"
        texto_centrado "{i}Prefirió entregarse y volver a prisión{/i}"
        "Bad Ending."
        return

    label ir_al_sur:
        scene bg boat

        contexto "Contexto: \n{i}Llega a un pequeño muelle...{/i}"

        anon_n "Perfecto, esto me sera útil..."

        contexto "Contexto: \n{i}Se sube a una lancha y arranca{/i}"

        anon_n "¡Hasta nunca, Idiotas!"

        contexto "Contexto: \n{i}se aleja en la lancha{/i}"

        menu:
            "¿Debería revisar las provisiones?"
            "Revisar ahora provisiones y nivel de combustible":
                jump revisar_provisiones
            "Revisar mas tarde":
                # Bad Ending
                texto_centrado "{i}No las revisa y se adentra en altamar{p}Al tercer día se queda sin provisiones{p}{/i}"
                texto_centrado "{i}Una semana después muere por el hambre y la insolación{/i}"
                "Bad Ending."
                return

    label revisar_provisiones:
        "Con esto podre vivir algunos días más"

        texto_centrado "{i}2 Días después...{/i}"

        menu:
            "El combustible esta empezando a escasear"
            "Aumentar Velocidad":
                # Bad ending
                texto_centrado "{i}Acelera la velocidad y queda sin combustible en altamar{/i}"
                texto_centrado "{i}Días después muere por falta de provisiones{/i}"
                "Bad Ending."
                return
            "Disminuir Velocidad":
                contexto "Contexto: \n{i}Observa un objeto a cierta distancia en el oceano...{/i}"
                menu:
                    "¿Pero qué es eso?, ¿será posible...?"
                    "Acercarse a examinar":
                        menu:
                            "¿Y este como logró llegar hasta aquí?"
                            "Rescatarlo":
                                contexto "{i}Rescata a una persona que flotaba aún con vida en el mar...{/i}"
                                contexto "{i}Algunos minutos después el naufrago despierta...{/i}"
                                show harrison one:
                                    ease .5 zoom 1.5 xoffset 700 yoffset 50
                                naufrago "¡No es posible! ¡¿{b}Ignacio Villanueva{/b}?!"
                                naufrago "¡Maldito Bastardo!"
                                show fugitive one:
                                    ease .5 zoom 1.5 xoffset 200 yoffset 50
                                anon_n "¡Es Don Nacho para tí!"
                                contexto "{i}Le da un puñetazo que lo hace caer{/i}"
                                naufrago "¡Me rompiste la nariz!"
                                narco "¡No exageres!, además, ¿quién se supone que eres tu?"
                                naufrago "¿Nunca has oido de mi?, Yo soy el gran {b}Robert \"Bobby\" Harrison{/b}"
                                narco "Ah, el loco de los barcos gigantes"
                                empresario "Prefiero el termino \"Excentrico\"... "
                                empresario "¡Hey!, ¿no se supone que deberías estar en prisión o algo?"
                                narco "Los tiempos han cambiado mi amigo, dime, ¿cómo es que alguien como tú terminó este lugar?"
                                "Good Ending."
                            "Dejarlo a su suerte":
                                # Bad ending
                                texto_centrado "{i}Al alejarse se dió cuenta que iba directo a un huracán..."
                                extend "{p}Intentó saltar, pero fue peor, murió ahogado y su cuerpo fue arrastrado por el huracán.{/i}"
                                "Bad Ending."
                                return
                    "Seguir otro rumbo":
                        # Bad ending
                        texto_centrado "{i}Terminó llegando a tierra firme y se dió cuenta que había vuelto al punto de inicio...{/i}"
                        texto_centrado "{i}Rápidamente fue descubierto por uno de los guardias que disparó sin dudar{/i}"
                        texto_centrado "{i}No logró llegar muy lejos, fue capturado y llevado a otra penitenciaría.{/i}"
                        "Bad Ending."
                        return

    # Se acaba el juego.
    "{b}Fin de la demo 0.1{/b}"
    return