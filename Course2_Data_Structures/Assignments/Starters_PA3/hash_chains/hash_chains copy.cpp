#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <sstream>

using std::string;
using std::vector;
using std::cin;

struct Query {
  string type, s;
  size_t ind;
};


class QueryProcessor {
  int bucket_count;
  std::vector< std::deque< std::string > > data_;
  std::vector<std::string> results;
  size_t hash_func( const string& s ) const
  {
    static const size_t multiplier = 263;
    static const size_t prime = 1000000007;
    unsigned long long hash = 0;
    for ( int i = static_cast< int >( s.size() ) - 1; i >= 0; --i ) hash = ( hash * multiplier + s[i] ) % prime;
    return hash % bucket_count;
  }

public:
  explicit QueryProcessor( int bucket_count )
    : bucket_count( bucket_count )
    , data_( bucket_count )
    , results()
  {
  }

  Query readQuery() const
  {
    Query query;
    cin >> query.type;
    if ( query.type != "check" )
      cin >> query.s;
    else
      cin >> query.ind;
    return query;
  }

  void writeSearchResult( bool was_found )
  {
    std::string result = was_found ? "yes" : "no";
    results.push_back( result );
  }

  void insert( const std::string &str )
  {
    int bc = hash_func( str );
    auto &q = data_[ bc ];
    if ( std::find( q.begin(), q.end(), str ) == q.end() )
      q.push_front( str );
  }

  std::string check( int ind )
  {
    std::stringstream ss;
    const auto &q = data_[ ind ];
    if ( q.empty() )
    {
      ss << "";
      return ss.str();
    }

    for ( auto it = q.begin(); it != q.end(); ++it )
    {
      ss << *it << " ";
    }
    return ss.str();
    ;
  }

  bool find( const std::string &str )
  {
    int bc = hash_func( str );
    const auto &q = data_[ bc ];
    auto it = std::find( q.begin(), q.end(), str );
    return it != q.end();
  }

  void del( const std::string &str )
  {
    int bc = hash_func( str );
    auto &q = data_[ bc ];
    auto it = std::find( q.begin(), q.end(), str );
    if ( it != q.end() )
      q.erase( it );
  }

  void processQuery( const Query& query )
  {
    if ( query.type == "check" ) {
      // use reverse order, because we append strings to the end
      /* for ( int i = static_cast< int >( elems.size() ) - 1; i >= 0; --i ) */
      /*   if ( hash_func( elems[i] ) == query.ind ) std::cout << elems[i] << " "; */
      auto es = check( query.ind );
      results.push_back( es );
    }
    else {
      /* vector< string >::iterator it = std::find( elems.begin(), elems.end(), query.s ); */
      if ( query.type == "find" )
        /* writeSearchResult( it != elems.end() ); */
        writeSearchResult( find( query.s ) );
      else if ( query.type == "add" ) {
        insert( query.s );
        /* if ( it == elems.end() ) elems.push_back( query.s ); */
      }
      else if ( query.type == "del" ) {
        /* if ( it != elems.end() ) elems.erase( it ); */
        del( query.s );
      }
    }
  }

  void processQueries()
  {
    int n;
    cin >> n;
    for ( int i = 0; i < n; ++i ) processQuery( readQuery() );

    for (const auto& r : results) {
      std::cout << r << "\n";
    }
  }
};

int main()
{
  std::ios_base::sync_with_stdio( false );
  int bucket_count;
  cin >> bucket_count;
  QueryProcessor proc( bucket_count );
  proc.processQueries();
  return 0;
}