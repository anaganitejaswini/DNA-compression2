#include<iostream>
#include<utility>

struct {
  static std::pair<double,double> getProbability( char c )
  {
    if (c >= 'A' && c <= 'Z')
      return std::make_pair( (c - 'A') * .01, (c - 'A') * .01 + .01);
    else
      throw "character out of range";
  }
} model;

double high = 1.0;
double low = 0.0;
char c;

while ( input >> c ) {
  std::pair<double, double> p = model.getProbability(c);
  double range = high - low;
  high = low + range * p.second;
  low = low + range * p.first; 
}
output << low + (high-low)/2;