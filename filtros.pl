% Base de datos de bebidas
bebida(agua, caliente, cena).
bebida(jugo_naranja, caliente, cena).
bebida(cafe, caliente, desayuno).
bebida(leche, natural, desayuno).
bebida(jugo_manzana, natural, almuerzo).
bebida(zumo_uva, natural, almuerzo).
bebida(refresco_cola, carbonatada, almuerzo).
bebida(te, caliente, almuerzo).
bebida(refresco_naranja, carbonatada, cena).
bebida(refresco_limón, carbonatada, cena).
bebida(te_verde, caliente, cena).
bebida(te_negro, caliente, cena).
bebida(leche_chocolate, con_lacteo, cena).

% Base de datos de proteínas
proteina(carne_res, roja, cena).
proteina(pollo, blanca, cena).
proteina(pescado, marino, cena).
proteina(cerdo, roja, almuerzo).
proteina(pavo, blanca, almuerzo).
proteina(atun, marino, cena).
proteina(lentejas, vegetariana, almuerzo).
proteina(salmon, marino, cena).
proteina(ternera, roja, cena).
proteina(huevo, blanca, desayuno).
proteina(camaron, marino, cena).

% Base de datos de acompañamientos
acompanamiento(ensalada, vegetales, almuerzo).
acompanamiento(papas_fritas, carbohidratos, almuerzo).
acompanamiento(arroz, carbohidratos, almuerzo).
acompanamiento(vegetal_al_vapor, vegetales, almuerzo).
acompanamiento(ensalada_de_tomate, vegetales, almuerzo).
acompanamiento(esparragos_gratinados, vegetales, almuerzo).
acompanamiento(puré_de_papas, carbohidratos, almuerzo).
acompanamiento(macarrones_con_queso, carbohidratos, almuerzo).
acompanamiento(pan_integral, carbohidratos, desayuno).
acompanamiento(sopa_de_tomate, calientes, cena).
acompanamiento(crema_de_brocoli, calientes, cena).
acompanamiento(papas_asadas, calientes, cena).

% Base de datos de postres
postre(queque, reposteria, desayuno).
postre(fruta, sin_lacteo, almuerzo).
postre(helado, con_lacteo, cena).
postre(tarta_manzana, con_lacteo, almuerzo).
postre(gelatina_frutas, sin_lacteo, almuerzo).
postre(tiramisu, con_lacteo, cena).
postre(flan, con_lacteo, cena).
postre(crema_cacahuate, sin_lacteo, cena).
postre(pudin_vainilla, con_lacteo, cena).
postre(tarta_fresa, con_lacteo, almuerzo).
postre(chocolate_caliente, con_lacteo, desayuno).
postre(helado_manzana, con_lacteo, almuerzo).


% Base de datos de calorías por platillo
calorias(agua, 0).
calorias(jugo_naranja, 120).
calorias(cafe, 2).
calorias(leche, 42).
calorias(jugo_manzana, 115).
calorias(zumo_uva, 154).
calorias(refresco_cola, 140).
calorias(te, 2).
calorias(refresco_naranja, 150).
calorias(refresco_limón, 135).
calorias(te_verde, 2).
calorias(te_negro, 2).
calorias(leche_chocolate, 208).
calorias(carne_res, 250).
calorias(pollo, 335).
calorias(pescado, 206).
calorias(cerdo, 242).
calorias(pavo, 135).
calorias(atun, 184).
calorias(lentejas, 230).
calorias(salmon, 367).
calorias(ternera, 250).
calorias(huevo, 68).
calorias(camaron, 99).
calorias(ensalada, 35).
calorias(papas_fritas, 365).
calorias(arroz, 130).
calorias(vegetal_al_vapor, 68).
calorias(ensalada_de_tomate, 78).
calorias(esparragos_gratinados, 124).
calorias(puré_de_papas, 143).
calorias(macarrones_con_queso, 350).
calorias(pan_integral, 80).
calorias(sopa_de_tomate, 74).
calorias(crema_de_brocoli, 103).
calorias(papas_asadas, 130).
calorias(queque, 350).
calorias(fruta, 120).
calorias(helado, 207).
calorias(tarta_manzana, 316).
calorias(gelatina_frutas, 62).
calorias(tiramisu, 280).
calorias(flan, 153).
calorias(crema_cacahuate, 400).
calorias(pudin_vainilla, 174).
calorias(tarta_fresa, 271).
calorias(chocolate_caliente, 192).
calorias(helado_manzana, 190).

% Regla para encontrar combinaciones que coincidan con las preferencias del cliente y mostrar los nombres con saltos de línea.
% combinacion_cliente(TipoBebida, TipoProteina, TipoAcompanamiento, TipoPostre, MomentoDelDia) :-
%    findall(Platillo, (
%        bebida(Bebida, TipoBebida, MomentoDelDia),
%        proteina(Proteina, TipoProteina, MomentoDelDia),
%        find_acompanamientos(Acompanamientos, TipoAcompanamiento,
%        MomentoDelDia),
%        find_postre(Postre, TipoPostre, MomentoDelDia),
%        list_to_set(Acompanamientos, AcompanamientosUnicos),
%        format(atom(Platillo), 'Bebida: ~w, Proteina: ~w,
%        Acompanamientos: ~w, Postre: ~w', [Bebida, Proteina,
%        AcompanamientosUnicos, Postre]),
%        writeln(Platillo), % Imprimir la combinación
%        nl % Salto de línea
%    ), _).


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



combinacion_cliente(TipoBebida, TipoProteina, TipoAcompanamiento, TipoPostre, MomentoDelDia, CaloriasMinimas) :-
    findall(Platillo, (
        bebida(Bebida, TipoBebida, MomentoDelDia),
        proteina(Proteina, TipoProteina, MomentoDelDia),
        find_acompanamientos(Acompanamientos, TipoAcompanamiento, MomentoDelDia),
        find_postre(Postre, TipoPostre, MomentoDelDia),
        list_to_set(Acompanamientos, AcompanamientosUnicos),
        calcular_total_calorias([Bebida, _|AcompanamientosUnicos], TotalCalorias),
        TotalCalorias =< CaloriasMinimas,
        format(atom(Platillo), 'Bebida: ~w, Proteina: ~w, Acompanamientos: ~w, Postre: ~w, Calorías: ~w', [Bebida, Proteina, AcompanamientosUnicos, Postre, TotalCalorias]),
        writeln(Platillo), % Imprimir la combinación
        nl % Salto de línea
    ), _).

calcular_total_calorias([], 0).
calcular_total_calorias([Alimento|Rest], TotalCalorias) :-
    calorias(Alimento, Calorias),
    calcular_total_calorias(Rest, RestCalorias),
    TotalCalorias is Calorias + RestCalorias.

combinaciones_diferentes_cliente(TipoBebida, TipoProteina, TipoAcompanamiento, TipoPostre, MomentoDelDia, CaloriasMinimas) :-
    findall(Platillo, (
        bebida(Bebida, TipoBebida, MomentoDelDia),
        proteina(Proteina, TipoProteina, MomentoDelDia),
        find_acompanamientos(Acompanamientos, TipoAcompanamiento, MomentoDelDia),
        find_postre(Postre, TipoPostre, MomentoDelDia),
        list_to_set(Acompanamientos, AcompanamientosUnicos),
        calcular_total_calorias([Bebida | AcompanamientosUnicos], TotalCalorias),
        TotalCalorias =< CaloriasMinimas,
        format(atom(Platillo), 'Bebida: ~w, Proteina: ~w, Acompanamientos: ~w, Postre: ~w, Calorías: ~w', [Bebida, Proteina, AcompanamientosUnicos, Postre, TotalCalorias])
    ), Combinaciones),
    obtener_10_combinaciones_diferentes(Combinaciones, 10, [], Resultado),
    imprimir_combinaciones(Resultado).

% Obtener 10 combinaciones diferentes
obtener_10_combinaciones_diferentes(_, 0, Resultado, Resultado).
obtener_10_combinaciones_diferentes(Combinaciones, N, ResultadoParcial, Resultado) :-
    N > 0,
    random_member(Comb, Combinaciones),
    \+ member(Comb, ResultadoParcial),
    N1 is N - 1,
    obtener_10_combinaciones_diferentes(Combinaciones, N1, [Comb | ResultadoParcial], Resultado).

% Imprimir combinaciones
imprimir_combinaciones([]).
imprimir_combinaciones([Comb | Resto]) :-
    writeln(Comb),
    imprimir_combinaciones(Resto).

