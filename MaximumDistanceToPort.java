import java.util.*;

public class MaximumDistanceToPort {
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();

        int[] productType = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            productType[i] = sc.nextInt();
        }

        List<Integer>[] graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph[u].add(v);
            graph[v].add(u);
        }

        int[] dist = bfs(1, n, graph);

        int[] maxDist = new int[k + 1];
        Arrays.fill(maxDist, -1);

        for (int i = 1; i <= n; i++) {
            int product = productType[i];
            maxDist[product] = Math.max(maxDist[product], dist[i]);
        }

        for (int i = 1; i <= k; i++) {
            System.out.print(maxDist[i] + " ");
        }
    }

    public static int[] bfs(int source, int n, List<Integer>[] graph) {
        int[] dist = new int[n + 1];
        Arrays.fill(dist, INF);
        dist[source] = 0;

        Queue<Integer> queue = new LinkedList<>();
        queue.add(source);

        while (!queue.isEmpty()) {
            int city = queue.poll();

            for (int neighbor : graph[city]) {
                if (dist[neighbor] == INF) {
                    dist[neighbor] = dist[city] + 1;
                    queue.add(neighbor);
                }
            }
        }

        return dist;
    }
}
