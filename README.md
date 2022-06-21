#include<iostream.h>

#include <list.h>

using namespace std;

class Gra 
{
  int numVer;
  list<int> *adjLists;
  bool *visi;
   public:
  Gra(int V);
  void add_Edge(int src, int dest);
  void DeFiSe(int vertex);
};
Gra::Gra(int vertices)
{
  numVer = vertices;
  adjLists = new list<int>[vertices];
  visi = new bool[vertices];
}
void Gra::add_Edge(int src, int dest)
{
  adjLists[src].push_front(dest);
}
void Gra::DeFiSe(int vertex) 
{
  visi[vertex] = true;
  list<int> adjList = adjLists[vertex];
  cout << vertex << " ";
  list<int>::iterator i;
  for (i = adjList.begin(); i != adjList.end(); ++i)
    if (!visi[*i])
      DeFiSe(*i);
}

int main()
{
  Gra g(4);
  g.add_Edge(0, 1);
  g.add_Edge(0, 2);
  g.add_Edge(1, 2);
  g.add_Edge(2, 3);
  g.add_Edge(2,1);
  cout<<"Depth First Search from vertex 2 is :"<<endl; 
  g.DeFiSe(2);

  return 0;
}

