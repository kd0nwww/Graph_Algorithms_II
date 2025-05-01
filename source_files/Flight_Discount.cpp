#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

typedef long long ll;
typedef pair<ll, int> pli;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    
    vector<vector<pair<int, ll>>> graph(n+1);
    vector<vector<pair<int, ll>>> reverse_graph(n+1);
    
    for (int i = 0; i < m; i++) {
        int a, b;
        ll c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
        reverse_graph[b].push_back({a, c});
    }
    
    const ll INF = 1e18;
    
    auto dijkstra = [&](const vector<vector<pair<int, ll>>>& g, int start) {
        vector<ll> dist(n+1, INF);
        dist[start] = 0;
        
        priority_queue<pli, vector<pli>, greater<pli>> pq;
        pq.push({0, start});
        
        while (!pq.empty()) {
            auto [d, node] = pq.top();
            pq.pop();
            
            if (d > dist[node])
                continue;
            
            for (auto [next_node, weight] : g[node]) {
                if (dist[node] + weight < dist[next_node]) {
                    dist[next_node] = dist[node] + weight;
                    pq.push({dist[next_node], next_node});
                }
            }
        }
        
        return dist;
    };

    vector<ll> dist_from_start = dijkstra(graph, 1);
    vector<ll> dist_from_end = dijkstra(reverse_graph, n);

    ll min_cost = INF;
    
    for (int a = 1; a <= n; a++) {
        if (dist_from_start[a] == INF)
            continue;
        
        for (auto [b, c] : graph[a]) {
            if (dist_from_end[b] == INF)
                continue;
       
            ll cost = dist_from_start[a] + (c / 2) + dist_from_end[b];
            min_cost = min(min_cost, cost);
        }
    }
    
    cout << min_cost << "\n";
    
    return 0;
}