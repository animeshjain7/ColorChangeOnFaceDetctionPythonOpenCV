# ColorChangeOnFaceDetctionPythonOpenCV
choose random color of rectangle at every iteration using #python #openCV #FaceDetection #haarcascades  

#### if you get this error => 'TypeError: Scalar value for argument 'color' is not numeric' 
this error is because rectangle function takes native python datatypes but np array creates datatype of its own type like :
* numpy.float32 ,
* numpy.float64 ,
* numpy.uint32 ,
* numpy.int16   

1 .tolist() => this function changes the np array into the list and also changes its datatype to scaler data type(or python native datatype)

2 without using np array three numbers can be generated using math and random module =>

 a = tuple(math.floor(random.random()*256),math.floor(random.random()*256),math.floor(random.random()*256))

a = (123,234,12)

# To close the camera window press x 
