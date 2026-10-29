List<List<String>> casos = new List<List<String>>{
    new List<String>{'conservador sem reserva', 'curto', 'nao', 'resgatar', 'nenhuma'},
    new List<String>{'arrojado com reserva', 'longo', 'sim', 'aplicar_mais', 'alguma'},
    new List<String>{'moderado acento maiuscula', 'Médio', 'parcial', 'esperar', 'pouca'},
    new List<String>{'arrojado sem reserva', 'longo', 'nao', 'aplicar_mais', 'alguma'},
    new List<String>{'resposta invalida', 'talvez', 'sim', 'esperar', 'pouca'}
};
for (List<String> c : casos) {
    Flow.Interview f = Flow.Interview.createInterview('Nu_Explica_Calcular_Perfil', new Map<String, Object>{
        'prazo' => c[1], 'reserva' => c[2], 'reacao_queda' => c[3], 'experiencia' => c[4]
    });
    f.start();
    System.debug('RESULTADO ' + c[0] + ': perfil=' + f.getVariableValue('perfil')
        + ' pontos=' + f.getVariableValue('pontuacao')
        + ' priorizar_reserva=' + f.getVariableValue('priorizar_reserva'));
}
