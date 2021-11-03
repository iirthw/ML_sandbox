# Readme

# On Converting Keras Saved Model to TensorFlow.js

Preliminaries:

- SavedModel is the universal serialization format for TensorFlow models.

- SavedModel provides a language-neutral format to save machine-learning models that is recoverable and hermetic. It enables higher-level systems and tools to produce, consume and transform TensorFlow models.
- .h5 file extension: You mean a HDF5/H5 file, which is a file format to store structured data, its not a model by itself. Keras saves models in this format as it can easily store the weights and model configuration in a single file.

**Converting an existing Keras model to TF.js Layers format**
`
# bash

tensorflowjs_converter --input_format keras \
                       path/to/my_model.h5 \
                       path/to/tfjs_target_dir
`

References

* SavedModel https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python/saved_model/
* Importing a Keras model into TensorFlow.js https://www.tensorflow.org/js/tutorials/conversion/import_keras
