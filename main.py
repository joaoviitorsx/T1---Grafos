from pathlib import Path

from algoritmos.graph import Graph
from estrutura.dfs import DepthFirstPaths
from estrutura.bfs import BreadthFirstPaths


STATE_TO_ID = {
    "AL": 0,
    "BA": 1,
    "CE": 2,
    "MA": 3,
    "PB": 4,
    "PE": 5,
    "PI": 6,
    "RN": 7,
    "SE": 8,
}

ID_TO_STATE = {v: k for k, v in STATE_TO_ID.items()}


def format_states(vertices):
    return " -> ".join(ID_TO_STATE[v] for v in vertices)


def read_state(prompt):
    while True:
        state = input(prompt).strip().upper()
        if state in STATE_TO_ID:
            return state
        print("Estado inválido. Use: AL, BA, CE, MA, PB, PE, PI, RN, SE.\n")


def print_section(title):
    print("\n" + "=" * 50)
    print(f"{title}")
    print("=" * 50)


def main():
    data_path = Path(__file__).resolve().parent.parent / "src" / "dados" / "nordeste.txt"
    graph = Graph.from_file(data_path)

    # Cabeçalho
    print("=" * 50)
    print("TRABALHO - BUSCAS EM GRAFOS (DFS e BFS)")
    print("=" * 50)

    # Mapeamento
    print_section("MAPEAMENTO DOS ESTADOS")
    for state, idx in STATE_TO_ID.items():
        print(f"{state} -> {idx}")

    # Entrada
    print_section("ENTRADA")
    origin = read_state("Digite o estado de origem: ")
    destination = read_state("Digite o estado de destino: ")

    source = STATE_TO_ID[origin]
    target = STATE_TO_ID[destination]

    # Execução
    dfs = DepthFirstPaths(graph, source)
    bfs = BreadthFirstPaths(graph, source)

    print_section("RESULTADOS")

    # 1. Existe caminho
    exists = dfs.has_path_to(target)
    print(f"[1] Existe caminho entre {origin} e {destination}?")
    print(f"    ➜ {'SIM' if exists else 'NÃO'}\n")

    # 2. Caminho DFS
    dfs_path = dfs.path_to(target)
    print("[2] Caminho encontrado (DFS):")
    if dfs_path:
        print(f"    ➜ {format_states(dfs_path)}")
    else:
        print("    ➜ Nenhum caminho encontrado")
    print()

    # 3. Caminho BFS
    bfs_path = bfs.path_to(target)
    print("[3] Caminho encontrado (BFS - menor caminho):")
    if bfs_path:
        print(f"    ➜ {format_states(bfs_path)}")
    else:
        print("    ➜ Nenhum caminho encontrado")
    print()

    # 4. Alcançáveis
    reachable = dfs.reachable_vertices()
    print("[4] Estados alcançáveis a partir da origem:")
    print(f"    ➜ {format_states(reachable)}\n")

    # 5. Ordem DFS
    print("[5] Ordem de visita (DFS):")
    print(f"    ➜ {format_states(dfs.visit_order())}\n")

    # 6. Ordem BFS
    print("[6] Ordem de visita (BFS):")
    print(f"    ➜ {format_states(bfs.visit_order())}")

if __name__ == "__main__":
    main()