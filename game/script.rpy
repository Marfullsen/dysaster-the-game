# Guión del juego.

# Inicialización de los elementos utilizados.
init:

    # Título de la ventana
    $ config.window_title = "Dysaster, the game - DevJam CITT 2021"

    # Tamaño de la pantalla.
    define width  = 1280
    define height = 720

    # Personajes principales.
    ##
    # Don Nacho
    define color_nombre_narco = "#FF8200"
    define anon_n = Character("???", color=color_nombre_narco)
    define narco = Character("Don Nacho", color=color_nombre_narco) # Ignacio Villanueva Alcallaga
    ##
    # Los demás.
    define naufrago = Character("Naufrago", color="#5599ff")
    define empresario = Character("Harrison", color="#5599ff") # Robert Bobby harrison
    define waton = Character("Jimeno") # Jimeno Montoya
    define mecanica = Character("Lili") # Liliana Oliviera

    # Personajes secundarios.
    define guardia_1 = Character("Guardia 1", color="#584f63")
    define guardia_2 = Character("Guardia 2", color="#aaa")
    define guardia_3 = Character("Guardia 3", color="#a52c2b")
    define guardia_4 = Character("Guardia 4", color="#a7a223")

    # Fondos de cada escena escalados.
    image bg guard_1 = im.Scale('bg guard_1.png', width, height)
    image bg guard_2 = im.Scale('bg guard_2.png', width, height)
    image bg guard_3 = im.Scale('bg guard_3.png', width, height)
    image bg guard_4 = im.Scale('bg guard_4.png', width, height)
    image bg prison = im.Scale('bg prison.jpg', width, height)
    image bg parking = im.Scale('bg parking.jpg', width, height)
    image bg norte_sur = im.Scale('bg norte_sur.png', width, height)
    image bg zombies = im.Scale('bg zombies.jpg', width, height)
    image bg boat = im.Scale('bg boat.jpg', width, height)
    image bg waves = im.Scale('bg waves.jpg', width, height)
    image bg bodega = im.Scale('bg bodega.png', width, height)
    image bg beach = im.Scale('bg beach.jpg', width, height)

    # Otras variables
    default items_bodega = set()

    # Textos del narrador & el contexto.
    define texto_centrado = Character(None, what_xalign=0.5, what_text_align=0.5, text_xpos=0.5, window_yalign=0.5)
    define contexto = Character(None, what_xalign=0.5, what_text_align=0.5, text_xpos=0.5, window_yalign=0.5, what_color="#e79600", what_italic=True)
    define warning_box = Character(None, window_xalign=0.5, window_yalign=0.5, what_xalign=0.5, what_yalign=0.5, text_xpos=0.5, text_ypos=0.5, what_text_align=0.5, interact=False)
    define warning_title = "{b}{color=#f00}Disclaimer{/color}{/b}"

# Se inicia el juego.
label start: #renpy-graphviz: TITLE
    $ save_name = "iNiCiO"

    # Detener la música del menú principal.
    stop music fadeout 2.0

    $ renpy.music.play('/audio/bg-theme.mp3')

    # Al inicio el fondo es de color negro.
    # Disclaimer
    warning_box "[warning_title]\n\
    El Siguiente trabajo es una obra de ficción que\
    puede contener material sensible y/u ofensivo\
    para algunas personas, cualquier parecido con\
    la realidad sobre personajes, diálogos, elementos\
    y/o historia es pura coincidencia. Todo el contenido\
    presentado en este juego es total y completamente\
    ficticio. Al haber iniciado el archivo ejecutable\
    del juego (dysaster.exe), usted renuncia automaticamente a\
    toda posible demanda u otra acción legal en contra\
    del Team Walala y a todos sus integrantes.\
    \n© 2021 Team Walala"

    pause(1.0)
    
    # Fondo prisión.
    scene bg prison

    # Hablado por narrador, centrado en el eje X e Y.
    texto_centrado "{i}Prisión de Guantánamo, Cuba{/i}"

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
        ease 1 zoom 1.5 xoffset 500 yoffset 50

    # Personaje principal inicia su diálogo.
    anon_n "¡Finalmente, después de 6 años, soy libre!"
    anon_n "¡Había estado esperando por este momento!"

    #contexto "Contexto: \n{i}Observando a lo lejos{/i}"

    anon_n "¡Dios, ya sabía acerca de esto, pero verlo en persona va más allá de mi imaginación!"

    scene bg zombies
    #contexto "Contexto: \n{i}Se acerca una horda de infectados{/i}"

    scene bg norte_sur

    $ save_name = "eL eScAPe"

    menu:
        "¿Hacia dónde debería correr?"
        "Correr hacia el norte":
            jump ir_al_norte
        "Correr hacia el sur":
            jump ir_al_sur

label ir_al_norte:

    contexto "Contexto: \n{i}Llega a un estacionamiento afuera de la prisión{/i}"
    scene bg parking
    anon_n "{i}(¡Necesito salir de aquí, pero ya!){/i}"
    contexto "Contexto: \n{i}Guardias se estan enfrentando con infectados{/i}"
    show fugitive one:
        xzoom -1.0
        linear .5 xalign .5
    pause .5
    show fugitive one:
        xzoom 1.0
        linear .5 xalign .5
    pause .5
    show fugitive one:
        xzoom -1.0
        linear .5 xalign .5
    pause .5
    show fugitive one:
        xzoom 1.0
        linear .5 xalign .5
    anon_n "Rayos, si me ven estoy perdido "
    contexto "Contexto: \n{i}se oculta detrás de un automóvil estacionado{/i}"

    contexto "Contexto: \n{i}Personas civiles tratan de huir del lugar{/i}"
    anon_n "¡Ábrete, ábrete! "
    contexto "Contexto: \n{i}Tratando de abrir la cerradura de un auto{/i}"

    anon_n "Ah, Maldita sea "
    contexto "Contexto: \n{i}Comienza a correr{/i}"

    contexto "Contexto: \n{i}Una niña choca con él mientras corre, empujándole{/i}"
    anon_n "Estúpida niña, fíjate por..."
    anon_n "Un momento... "
    contexto "Contexto: \n{i}Se da cuenta que tiene una herida en su pierna{/i}"

    anon_n "Ya veo"
    contexto "Contexto: \n{i}La niña pequeña resultó ser una infectada y una horda ya ha rodeado al prisionero{/i}"
    anon_n "¿Con que así va a ser, verdad? "
    contexto "Contexto: \n{i}Saca un cuchillo oculto en su guante{/i}"

    anon_n "¿Y qué estan esperando bastardos? ¡¡vengan por mí, que hoy es un gran día para morir!!"
    contexto "Contexto: \n{i}Se lanza a pelear con los infectados{/i}"
    contexto "Contexto: \n{i}Después de un rato, tras estar luchando contra los infectados,{p}termina completamente agotado y cae al piso, mueriendo casi al instante{/i}"

    "Bad Ending."
    jump fin

label ir_al_sur:
    scene bg boat

    #contexto "Contexto: \n{i}Llega a un pequeño muelle...{/i}"
    show lancha agua:
        ease 1 zoom 1.0 xoffset 300 yoffset 300

    anon_n "¡Perfecto, esto me será útil!"

    #contexto "Contexto: \n{i}Encuentra una lancha{/i}"

    menu:
        "¿Debería revisar las provisiones?"
        "Revisar ahora provisiones y nivel de combustible":
            jump revisar_provisiones
        "Revisar mas tarde":
            # Bad Ending
            jump revisar_después

label revisar_después:
    contexto "Contexto: \n{i}Se sube a una lancha y arranca{/i}"
    anon_n "¡Hasta nunca, Idiotas!"
    contexto "Contexto: \n{i}se aleja en la lancha{/i}"
    texto_centrado "{i}No las revisa y se adentra en altamar{p}Al tercer día se queda sin provisiones{p}{/i}"
    texto_centrado "{i}Una semana después muere por el hambre y la insolación{/i}"
    "Bad Ending."
    jump fin

label revisar_provisiones:
    "Con esto podré vivir algunos días más"

    #contexto "Contexto: \n{i}Se sube a una lancha y arranca{/i}"

    anon_n "¡Hasta nunca, Idiotas!"

    #contexto "Contexto: \n{i}se aleja en la lancha{/i}"

    scene black
    texto_centrado "{i}2 Días después...{/i}"
    scene bg boat

    menu:
        "El combustible esta empezando a escasear"
        "Aumentar Velocidad":
            jump ir_más_rápido
        "Disminuir Velocidad":
            jump ir_más_lento

label ir_más_rápido:    
    # Bad ending
    texto_centrado "{i}Acelera la velocidad y queda sin combustible en altamar{/i}"
    texto_centrado "{i}Días después muere por falta de provisiones{/i}"
    "Bad Ending."
    jump fin

label ir_más_lento:
    contexto "Contexto: \n{i}Observa un objeto a cierta distancia en el oceano...{/i}"
    # contexto "Contexto: \n{i}{/i}"
    menu:
        "¿Pero qué es eso?, ¿será posible...?"
        "Acercarse a examinar":
            jump examinar
        "Seguir otro rumbo":
            jump seguir_otro_rumbo

label seguir_otro_rumbo:
    # Bad ending
    texto_centrado "{i}Terminó llegando a tierra firme y se dió cuenta que había vuelto al punto de inicio...{/i}"
    texto_centrado "{i}Rápidamente fue descubierto por uno de los guardias que disparó sin dudar{/i}"
    texto_centrado "{i}No logró llegar muy lejos, fue capturado y llevado a otra penitenciaría.{/i}"
    "Bad Ending."
    jump fin

label examinar:
    contexto "Contexto: \n{i}Apenas logra distinguir lo que parece una persona que él conocía...{/i}"
    menu:
        "¿Y este como logró llegar hasta aquí?"
        "Rescatarlo":
            $ save_name = "SeGunDo-PeRsOnAjE"
            jump rescatarlo
        "Dejarlo a su suerte":
            jump dejarlo

label rescatarlo:
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
    narco "¡No exageres!, además, ¿quién se supone que eres tú?"
    naufrago "¿Nunca has oido de mi?, Yo soy el gran {b}Robert \"Bobby\" Harrison{/b}"
    narco "Ah, el loco de los barcos gigantes"
    empresario "Prefiero el termino \"Excentrico\"... "
    empresario "¡Hey!, ¿no se supone que deberías estar en prisión o algo?"
    narco "Los tiempos han cambiado mi amigo, dime, ¿cómo es que alguien como tú terminó este lugar?"

    empresario "Bueno..."
    empresario "En verdad es algo vergonzoso de admitir..."
    empresario "Pero como tú ya sabrás, hace 6 años cuando condenaste al mundo a este apocalipsis zombie, o algo así..."
    narco "¡Que soy inocente maldita sea, y siempre lo he sido!"
    empresario "Como sea, me di la tarea de intentar salvar la mayor cantidad de vidas posibles"
    empresario "Construyendo una flota de super cruceros o ciudades flotantes como me gusta llamarlas a mí"
    empresario "En donde la humanidad podría vivir tranquila y sin tener que preocuparse por esos infectados"
    empresario "Pues es más que obvio que alguno de ellos jamás aparecería en medio del mar ..."

    # Segunda parte
    narco "¡Ve al grano de una vez y ya!"
    empresario "Vaya tipo más impaciente, en fin, hace poco realizamos en mi crucero personal una gran celebración"
    empresario "Debí de haber bebido mucho alcohol porque lo último que recuerdo es que estaba sentando en una baranda cantando"
    empresario "Quizá perdí el equilibrio lo que llevó a que me cayera al mar"
    narco "..."
    narco "¿Aún tienen alcohol después de todos estos años?"
    empresario "Eh..."
    empresario "Cambiando de tema, necesito regresar a mi barco así que voy a necesitar un aventón"
    empresario "¿Qué me dices?, ¿podrías ayudarme a volver?"
    empresario "Sería por unos buenos billetes o si lo prefieres puedo conseguirte una de las mejores habitaciones en mi barco"
    empresario "¿Qué te parece?"
    narco "Veo que ustedes los {i}snobs{/i} nunca salen de sus burbujas"
    narco "Primero, el dinero en esta era no es nada más que un simple papel sin valor"
    narco "Segundo, no tengo ni la menor idea en dónde pueda estar tu susodicho crucero y creo que tú tampoco"
    narco "Y tercero, ahora que estás aquí, tanto mis provisiones como el combustible de esta lancha estan al mínimo"
    narco "así que a menos que encontremos algo para reabastecernos, dudo que lleguemos con vida a la próxima semana"
    empresario "..."
    scene black
    texto_centrado "Esa misma noche..."
    scene bg waves
    contexto "Una feroz tormenta en altamar"
    empresario "¡¡Vamos a morir!!"
    narco "¡Cierra el hocico y sujétate de algo, no he llegado tan lejos solo para terminar muriendo por una maldita tormenta!"
    narco "Como si algo como esto pudiera detenerme"

    #contexto "Una enorme ola está por golpear la lancha"

    empresario "¡Gira!, ¡¡GIRA!!"
    contexto "La ola hunde la lancha"

    scene bg beach
    #contexto "Contexto: Llegan a una playa pequeña"

    show harrison one:
        ease .5 zoom 1.5 xoffset 800 yoffset 50

    # Tercera parte
    empresario "¡Cómo me duele la cabeza!"
    empresario "Hmm... ¿en dónde está ese sujeto?"
    contexto "Don Nacho a lo lejos observando hacia el horizonte"
    show fugitive one:
        ease .5 zoom 1.5 xoffset 100 yoffset 50
    narco "¿Sigues con vida, eh?"
    empresario "¿Alguna idea de dónde estamos?"
    narco "Colombia"
    empresario "¿Y cómo lo sabes?"
    narco "¿Ves ese lugar al otro lado del mar?"
    narco "ese lugar es Puerto Bolivar, lo sé porque era uno de los puertos que solía usar en mi ruta de tráfico"
    empresario "¿Y ahora qué?"
    narco "Hay que ir para allá, pues de seguro debe haber comida o herramientas que nos puedan ser de utilidad"
    menu:
        "Ir por Tierra":
            jump tierra
        "Ir por Mar":
            jump mar

label dejarlo:
    # Bad ending
    texto_centrado "{i}Al alejarse se dió cuenta que iba directo a un huracán..."
    extend "{p}Intentó saltar, pero fue peor, murió ahogado y su cuerpo fue arrastrado por el huracán.{/i}"
    "Bad Ending."
    jump fin

label tierra:
    # Bad Ending
    "Se mueren"
    "Bad ending"
    jump fin

label mar:
    contexto "Don Nacho se tira al mar"
    empresario "¿Qué estas haciendo?"
    narco "Es más seguro ir nadando hasta allí que ir por tierra, a menos que te quieras encontrar con algún infectado"
    empresario "¿Acaso no podemos ir en un bote o algo?"
    narco "Parece que no tenemos una embarcación ..."
    narco "Por si no lo has notado, la tormenta no solo hundió la lancha"
    narco "También se llevó las pocas provisiones que iban quedando, así que no hay de otra"
    narco "Pero si prefieres quedarte aquí, es cosa tuya"
    empresario "¡Espera un momento!"
    narco "¿Ahora qué quieres?, ¿acaso no sabes nadar?"
    empresario "¡Pues claro que si sé!"
    narco "¿Entonces...?"
    empresario "¡Al demonio con esto!"
    contexto "Harrison se lanza al mar"
    contexto "Ambos hombres comienzan a nadar en dirección a Puerto Bolivar"
    scene black
    texto_centrado "Horas más tarde..."
    contexto "Puerto Bolivar, tras haber estado buscando por provisiones y herramientas por horas"
    empresario "¡Encontré algo!, ¡ayúdame a levantar esto!"
    narco "Vaya vaya, con que aquí se escondía"
    scene bg bodega
    show harrison one:
        ease .5 zoom 1.5 xoffset 700 yoffset 50
    show fugitive one:
        ease .5 zoom 1.5 xoffset 200 yoffset 50
    empresario "¿Sabes lo que es?"
    narco "La entrada secreta a una bodega subterránea que solían usar mis hombres en el pasado"
    narco "De seguro puede que aún deban haber algunos objetos interesantes allí dentro"
    empresario "Realmente está oscuro aquí"
    menu:
        "Usar una linterna":
            jump linterna
        "Usar un encendedor":
            jump encendedor

label linterna:
    narco "Este lugar tiene demasiado olor a metano"
    narco  "¡Y con razón, estas latas de gas están rotas!"
    empresario "¡Tomemos lo que podamos y largémonos!"
    narco "¡No, es mejor revisarlo todo primero para después no tener que terminar cargando peso muerto!"
    $ save_name = "ReViSaR_CajAs"
    $ items = 6
    while items:
        $ items -= 1
        menu:
            set items_bodega
            "Revisar cajas de madera":
                play sound "/audio/ding-effect.mp3"
                texto_centrado "Alimentos en conserva y otras provisiones encontradas"
            "Revisar cajas de carton":
                play sound "/audio/ding-effect.mp3"
                texto_centrado "Botiquines y medicinas encontradas"
            "Revisar pequeña caja de metal":
                play sound "/audio/gun-reload.mp3"
                texto_centrado "Pistolas 9mm encontradas"
                if "Revisar pequeño cilindro de metal" in items_bodega:
                    narco "¡Ahora si, con esto mejora nuestra suerte!"
                else:
                    empresario "Muy lindo pero... ¿dónde estan las balas?"
            "Revisar caja de plastico":
                play sound "/audio/ding-effect.mp3"
                texto_centrado "Cuchillos encontrados"
            "Revisar pequeño cilindro de metal":
                play sound "/audio/doble-bell-effect.mp3"
                texto_centrado "15 balas encontradas"
                if "Revisar pequeña caja de metal" not in items_bodega:
                    empresario "¿Balas? ¡perfecto, sólo faltan las armas!"
                else:
                    narco "No son muchas, pero aun asi servirán"
            "Revisar hielera":
                play sound "/audio/ding-effect.mp3"
                texto_centrado "Agua embotellada encontrada"

    narco "Con esto sera suficiente"
    empresario "Bien, mejor que nos largemos cuanto antes de aquí, este lugar me eseta dando escalofríos"
    narco "Primero hay que encontrar algún vehículo, sino dudo que podamos salir intactos de esta zona"
    scene bg zombies
    contexto "Una horda de infectados se esta acercando al área"
    scene bg bodega
    empresario "Ya anocheció"
    narco "¡Hay que andar con cautela, si hay infectados cerca, estamos bien jodidos, esos bastardos son más letales en la oscuridad!"
    scene bg zombies
    contexto "Ambos hombres salen de la bodega"
    empresario "¡Oh,no! ¡Mira hacia allá, infectados!"
    narco "Espera, no saben que nos encontramos aquí... Aun..."
    empresario "¡¡Estamos perdidos!!, ¡es nuestro fin!"
    scene black
    texto_centrado "Continuará...{p}(sólo si ganamos la DevJam ;) )"
    "Good Ending."
    jump fin

label encendedor:
    # Bad Ending
    "Explotan"
    "Bad Ending"
    jump fin

label fin: # renpy-graphviz: GAMEOVER
    # Se acaba el juego.
    "{b}Fin de la demo 0.1{/b}"
    return