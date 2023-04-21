## Tarefa 002 - 17/04/2022 - Pesquisa Rest API

1. Elaborar uma pesquisa sobre o tema "_Rest API_".
2. Elaborar um texto **no formato markdown** de pelo menos uma página, descrito com suas próprias palavras, destacando:
* As definições dos conceitos envolvidos;
* As principais características deste conceito (pelo menos umas cinco).

A arquitetura REST é simples e fornece acesso aos recursos para que o cliente REST acesse e renderize os recursos no lado do cliente. No estilo REST, URI ou IDs globais ajudam a identificar cada recurso.

Uma REST API é um conjunto de diretrizes para criar serviços web que permitem que aplicativos se comuniquem entre si através da Internet. A REST API é baseada no protocolo HTTP, que é usado para enviar e receber dados na Web.

Uma REST API é construída em torno de recursos, que são objetos ou dados que podem ser acessados através de uma URL exclusiva. Cada recurso pode ser manipulado usando uma combinação de quatro verbos HTTP básicos: GET, POST, PUT e DELETE.

Uma requisição REST basicamente consiste em:
Um verbo ou método HTTP, que define que tipo de operação o servidor vai realizar;
Um header, com o cabeçalho da requisição que passa informações sobre a requisição;
Um path (caminho ou rota) para o servidor, onde esta API será consumida
Informação no corpo da requisição (body), sendo esta informação opcional, geralmente enviado em formato JSON.

O método GET é usado para recuperar informações de um recurso, enquanto o método POST é usado para criar novos recursos. O método PUT é usado para atualizar um recurso existente e o método DELETE é usado para excluir um recurso.

Uma REST API bem projetada deve ser independente de plataforma e linguagem de programação, e deve ser fácil de usar e entender. Os desenvolvedores podem usar a REST API para criar aplicativos que se integram com outros serviços web, como serviços de mídia social, como a API do Facebook, e até meramente para estudos, com API's "engraçadas" como a Dog API ou a Star Wars API.

A REST API é amplamente utilizada na indústria de tecnologia e é considerada uma das melhores práticas para criar serviços web escaláveis e flexíveis. No entanto, é importante notar que a implementação de uma REST API pode ser complexa e requer um conhecimento aprofundado do protocolo HTTP e das diretrizes REST.

Os protocolos HTTP mais comuns se dividem em 200 (Sucesso), 400(Erro na requisição) ou 500(Erro interno do servidor).
