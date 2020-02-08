.. currentmodule:: Arithmos.data

#########################
Data Filters (``filter``)
#########################

Instances of classes derived from `Filter` are used for filtering the data.

When called with an individual data instance (:obj:`Arithmos.data.Instance`),
they accept or reject the instance by returning either `True` or `False`.

When called with a data storage (e.g. an instance of
:obj:`Arithmos.data.Table`) they check whether the corresponding class
provides the method that implements the particular filter. If so, the
method is called and the result should be of the same type as the
storage; e.g., filter methods of :obj:`Arithmos.data.Table` return new
instances of :obj:`Arithmos.data.Table`, and filter methods of SQL proxies
return new SQL proxies.

If the class corresponding to the storage does not implement a particular
filter, the fallback computes the indices of the rows to be selected and
returns `data[indices]`.


.. automodule:: Arithmos.data.filter
    :members: