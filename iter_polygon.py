class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [self.Polygon(i, R,self) for i in range(3, m+1)]
        
    def __len__(self):
        return self._m - 2
    
    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'
    
    def __getitem__(self, s):
        return self._polygons[s]
        
    def __iter__(self):
        print("Calling instance __iter__")
        return self.Polygon(self._m,self._R,self)
    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons, 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]
    class Polygon:
      def __init__(self, n, R, obj):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        self._obj = obj
        self._index = 0
        
      def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
      def __next__(self):
            print("Calling Iterator __next__")
            if self._index >= len(self._obj):
                raise StopIteration
            else:
                item = self._obj._polygons[self._index]
                self._index += 1
                return item
      @property
      def count_vertices(self):
        return self._n
    
      @property
      def count_edges(self):
        return self._n
    
      @property
      def circumradius(self):
        return self._R
    
      @property
      def interior_angle(self):
        return (self._n - 2) * 180 / self._n

      @property
      def side_length(self):
        return 2 * self._R * math.sin(math.pi / self._n)
    
      @property
      def apothem(self):
        return self._R * math.cos(math.pi / self._n)
    
      @property
      def area(self):
        return self._n / 2 * self.side_length * self.apothem
    
      @property
      def perimeter(self):
        return self._n * self.side_length
    
      def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
      def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented
