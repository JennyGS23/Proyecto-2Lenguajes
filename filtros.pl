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

% Obtener 10 combinaciones diferentes
obtener_10_combinaciones_diferentes(Combinaciones, 10, Resultado) :-
    obtener_10_combinaciones(Combinaciones, 10, Resultado).

obtener_10_combinaciones(_, 0, []).
obtener_10_combinaciones(Combinaciones, N, [Comb | Resultado]) :-
    N > 0,
    random_member(Comb, Combinaciones),
    N1 is N - 1,
    obtener_10_combinaciones(Combinaciones, N1, Resultado).


% Combinaciones diferentes del cliente
combinaciones_diferentes_cliente(TipoBebida, TipoProteina, TipoAcompanamiento, TipoPostre, MomentoDelDia, CaloriasMinimas) :-
    findall(Platillo, (
        (
            (MomentoDelDia = cena ; MomentoDelDia = general),
            (bebida(Bebida, TipoBebida, general) ; bebida(Bebida, TipoBebida, cena)),
            (proteina(Proteina, TipoProteina, general) ; proteina(Proteina, TipoProteina, cena)),
            find_acompanamientos(Acompanamientos, TipoAcompanamiento, MomentoDelDia),
            find_postre(Postre, TipoPostre, MomentoDelDia),
            list_to_set(Acompanamientos, AcompanamientosUnicos),
            calcular_total_calorias([Bebida | AcompanamientosUnicos], TotalCalorias),
            TotalCalorias =< CaloriasMinimas,
            format(atom(Platillo), 'Bebida: ~w, Proteina: ~w, Acompanamientos: ~w, Postre: ~w, Calorias: ~w', [Bebida, Proteina, AcompanamientosUnicos, Postre, TotalCalorias])
            %writeln(Platillo) % Imprimir la combinación
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
            format(atom(Platillo), 'Bebida: ~w, Proteina: ~w, Acompanamientos: ~w, Postre: ~w, Calorias: ~w', [Bebida, Proteina, AcompanamientosUnicos, Postre, TotalCalorias])
            %writeln(Platillo) % Imprimir la combinación
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
            format(atom(Platillo), 'Bebida: ~w, Proteina: ~w, Acompanamientos: ~w, Postre: ~w, Calorias: ~w', [Bebida, Proteina, AcompanamientosUnicos, Postre, TotalCalorias])
            %writeln(Platillo) % Imprimir la combinación
        )
    ), Combinaciones),
    obtener_10_combinaciones_diferentes(Combinaciones, 10, Resultado),
    imprimir_combinaciones(Resultado),!.




% Imprimir combinaciones
imprimir_combinaciones([]).
imprimir_combinaciones([Comb | Resto]) :-
    writeln(Comb),
    imprimir_combinaciones(Resto).






