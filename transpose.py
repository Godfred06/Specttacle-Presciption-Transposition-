

class Transpose:
  '''Class that takes the prescription and transposes it '''

    def __init__(self, sph, cyl, axis):
        self.sph= float(sph)
        self.cyl= float(cyl)
        self.axis= float(axis)
        self.new_cyl=None
        self.new_sph = None
        self.new_axis= None

    def trans_sph_cyl (self):
        '''Takes the sphere and cylindrical components of the prescription and transposes it'''
        self.new_sph= self.sph+self.cyl
        self.new_cyl= float(-self.cyl)
        return self.new_sph, self.new_cyl

    def trans_axis(self):
        '''Takes the axis of the prescription and transposes it'''
        if self.axis > 90 and self.axis<180:
            self.new_axis= self.axis-90
            return self.new_axis
        elif self.axis<90 or self.axis==90:
            self.new_axis = 90 + self.axis 
            return self.new_axis
        return 'Invalid input of the axis. Axis cannot be more than 180'

    def __str__ (self):
      '''Returns a string of the transposed prescription in the standard format as known by Optometrists'''
        return 'The newly transposed is {} / {} X {}'.format(str(self.new_sph),str(self.new_cyl),str(self.new_axis))



try:
    sphere = float( input('Enter your the sphere component of the prescription'))
except:
    print('Sphere component has to be a numerical value') 

try:
    cylinder= float(input('Enter the cylindrical component of the prescription'))
except:
     
    print('Cylindrical component has to be a numerical value')   
    raise ValueError
    
try:
    axis = float(input('Enter the axis of the prescription') )

except:
    print('Axis has to be a number ')
    raise ValueError     


try1 = Transpose(sphere,cylinder,axis)  
try1.trans_sph_cyl()
try1.trans_axis()
print(try1)


     
