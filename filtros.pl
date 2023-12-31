:- consult('datos.pl'). % Cargar los hechos desde datos.pl

acompanamiento(Alimento, TipoAcompanamiento, MomentoDelDia) :-
    elementoComida(Alimento, acompanamiento, TipoAcompanamiento, MomentoDelDia).
bebida(Alimento, TipoBebida, MomentoDelDia) :-
    elementoComida(Alimento, bebida, TipoBebida, MomentoDelDia).
proteina(Alimento, TipoProteina, MomentoDelDia) :-
    elementoComida(Alimento, proteina, TipoProteina, MomentoDelDia).
postre(Alimento, TipoPostre, MomentoDelDia) :-
    elementoComida(Alimento, postre, TipoPostre, MomentoDelDia).


find_acompanamientos(Acompanamientos, TipoAcompanamiento, MomentoDelDia) :-
    find_acompanamientos([], Acompanamientos, 3, TipoAcompanamiento, MomentoDelDia).

find_acompanamientos(Acc, Acc, 0, _, _).
find_acompanamientos(Acc, [A|Rest], N, TipoAcompanamiento, MomentoDelDia) :-
    N > 0,
    acompanamiento(A, TipoAcompanamiento, MomentoDelDia),
    N1 is N - 1,
    find_acompanamientos([A|Acc], Rest, N1, TipoAcompanamiento, MomentoDelDia).
find_acompanamientos(Acc, Rest, N, TipoAcompanamiento, MomentoDelDia) :-
    N > 0,
    \+ acompanamiento(_, TipoAcompanamiento, MomentoDelDia),
    find_acompanamientos(Acc, Rest, N, TipoAcompanamiento, MomentoDelDia).

find_postre(Postre, TipoPostre, MomentoDelDia) :-
    postre(Postre, TipoPostre, MomentoDelDia).
find_postre(Postre, TipoPostre, MomentoDelDia) :-
    \+ postre(_, TipoPostre, MomentoDelDia),
    Postre = sin_postre.


calcular_total_calorias([], 0).
calcular_total_calorias([Alimento|Rest], TotalCalorias) :-
    calorias(Alimento, Calorias),
    calcular_total_calorias(Rest, RestCalorias),
    TotalCalorias is Calorias + RestCalorias.


calcular_costo_total([], 0).
calcular_costo_total([Alimento|Resto], CostoTotal) :-
    precio(Alimento, Precio),
    calcular_costo_total(Resto, CostoResto),
    CostoTotal is Precio + CostoResto.

% Obtener 10 combinaciones diferentes
obtener_10_combinaciones_diferentes(Combinaciones, 10, Resultado) :-
    obtener_10_combinaciones(Combinaciones, 10, Resultado).

obtener_10_combinaciones(_, 0, []).
obtener_10_combinaciones(Combinaciones, N, [Comb | Resultado]) :-
    N > 0,
    random_member(Comb, Combinaciones),
    N1 is N - 1,
    obtener_10_combinaciones(Combinaciones, N1, Resultado).

% Abre el archivo para escritura
abrir_archivo :-
    open('combinaciones.txt', write, Archivo),
    tell(Archivo).

% Cierra el archivo
cerrar_archivo :-
    told.

combinaciones_diferentes_cliente(TipoBebida, TipoProteina, TipoAcompanamiento, TipoPostre, MomentoDelDia, CaloriasMinimas) :-
    abrir_archivo,
    findall([Platillo, PrecioTotal], (
        (
            (MomentoDelDia = cena ; MomentoDelDia = general),
            (bebida(Bebida, TipoBebida, general) ; bebida(Bebida, TipoBebida, cena)),
            (proteina(Proteina, TipoProteina, general) ; proteina(Proteina, TipoProteina, cena)),
            find_acompanamientos(Acompanamientos, TipoAcompanamiento, MomentoDelDia),
            find_postre(Postre, TipoPostre, MomentoDelDia),
            list_to_set(Acompanamientos, AcompanamientosUnicos),
            calcular_total_calorias([Bebida | AcompanamientosUnicos], TotalCalorias),
            TotalCalorias =< CaloriasMinimas,
            calcular_costo_total([Bebida, Proteina | AcompanamientosUnicos], PrecioTotal),
            format(atom(Platillo), 'Bebida: ~w, Proteina: ~w, Acompanamientos: ~w, Postre: ~w, Calorias: ~w', [Bebida, Proteina, AcompanamientosUnicos, Postre, TotalCalorias])
        )
        ;
        (
            (MomentoDelDia = desayuno ; MomentoDelDia = general),
            (bebida(Bebida, TipoBebida, general) ; bebida(Bebida, TipoBebida, desayuno)),
            (proteina(Proteina, TipoProteina, general) ; proteina(Proteina, TipoProteina, desayuno)),
            find_acompanamientos(Acompanamientos, TipoAcompanamiento, MomentoDelDia),
            find_postre(Postre, TipoPostre, MomentoDelDia),
            list_to_set(Acompanamientos, AcompanamientosUnicos),
            calcular_total_calorias([Bebida | AcompanamientosUnicos], TotalCalorias),
            TotalCalorias =< CaloriasMinimas,
            calcular_costo_total([Bebida, Proteina | AcompanamientosUnicos], PrecioTotal),
            format(atom(Platillo), 'Bebida: ~w, Proteina: ~w, Acompanamientos: ~w, Postre: ~w, Calorias: ~w', [Bebida, Proteina, AcompanamientosUnicos, Postre, TotalCalorias])
        )
        ;
        (
            (MomentoDelDia = almuerzo ; MomentoDelDia = general),
            (bebida(Bebida, TipoBebida, general) ; bebida(Bebida, TipoBebida, almuerzo)),
            (proteina(Proteina, TipoProteina, general) ; proteina(Proteina, TipoProteina, almuerzo)),
            find_acompanamientos(Acompanamientos, TipoAcompanamiento, MomentoDelDia),
            find_postre(Postre, TipoPostre, MomentoDelDia),
            list_to_set(Acompanamientos, AcompanamientosUnicos),
            calcular_total_calorias([Bebida | AcompanamientosUnicos], TotalCalorias),
            TotalCalorias =< CaloriasMinimas,
            calcular_costo_total([Bebida, Proteina | AcompanamientosUnicos], PrecioTotal),
            format(atom(Platillo), 'Bebida: ~w, Proteina: ~w, Acompanamientos: ~w, Postre: ~w, Calorias: ~w', [Bebida, Proteina, AcompanamientosUnicos, Postre, TotalCalorias])
        )
    ), CombinacionesConPrecio),
    obtener_10_combinaciones_diferentes(CombinacionesConPrecio, 10, Resultado),
    imprimir_combinaciones(Resultado),
    cerrar_archivo, !.

% Regla para imprimir combinaciones con precio
imprimir_combinaciones([]).
imprimir_combinaciones([[Comb, Precio] | Resto]) :-
    format('~w, Precio: ~w~n', [Comb, Precio]),
    imprimir_combinaciones(Resto).
