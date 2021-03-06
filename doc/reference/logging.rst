.. imprint: a program for creating documents from data and content templates

.. Copyright (C) 2019  Joseph R. Fox-Rabinovitz <jfoxrabinovitz at gmail dot com>

.. This program is free software: you can redistribute it and/or modify
.. it under the terms of the GNU Affero General Public License as
.. published by the Free Software Foundation, either version 3 of the
.. License, or (at your option) any later version.

.. This program is distributed in the hope that it will be useful,
.. but WITHOUT ANY WARRANTY; without even the implied warranty of
.. MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
.. GNU Affero General Public License for more details.

.. Author: Joseph Fox-Rabinovitz <jfoxrabinovitz at gmail dot com>
.. Version: 13 Apr 2019: Initial Coding


.. _logging:

=======
Logging
=======

The program log is one of the :ref:`outputs <introduction-layers-output>` of
Imprint. It is generated by the :ref:`engine <introduction-layers-engine>` and
:ref:`plugins <introduction-layers-plugins>`. The log provides traceability
into the workings of Imprint, including plugins. As an important part of the
user interaction on many levels, a separate document to describe the logging
facility is merited.


.. _logging-toc:

.. contents:: Contents
   :depth: 2
   :local:


.. _logging-configuration:

-------------
Configuration
-------------

Logging is configured through the :ref:`configuration-ipc`. The following
keywords are used to configure the logging output:

- :ref:`keywords-system-log_file`
- :ref:`keywords-system-file_level`
- :ref:`keywords-system-log_stderr`
- :ref:`keywords-system-stderr_level`
- :ref:`keywords-system-log_stdout`
- :ref:`keywords-system-stdout_level`
- :ref:`keywords-system-log_format`
- :ref:`keywords-system-log_images`

All keywords are optional. The default is to log ``WARNING`` and worse to
:py:obj:`~sys.stdout`. If :ref:`keywords-system-log_stderr` is set to
:py:obj:`True`, messages with level ``ERROR`` and worse will  be sent to
:py:obj:`~sys.stderr` instead. In general, when both
:ref:`keywords-system-stdout_level` and :ref:`keywords-system-stderr_level` are
:py:obj:`True`, :py:obj:`~sys.stdout` will receive only the messages with
levels greater than or equal to :ref:`keywords-system-stdout_level`, but
strictly less than :ref:`keywords-system-stderr_level`.

If :ref:`keywords-system-log_file` is set to a non-empty string, all messages
will be logged to it regardless of what is written to :py:obj:`~sys.stdout` and
:py:obj:`~sys.stderr`.

The logging format can be controlled by :ref:`keywords-system-log_format`, which
is the same type of string that can be passed in to `format` argument of
:py:func:`logging.basicConfig` or the `fmt` argument of
:py:class:`logging.Formatter`. The template is a ``%``-interpolated format
string that refers to the attributes of a :py:class:`logging.LogRecord` by name.


.. _logging-images:

-------------
Image Logging
-------------

If the keyword :ref:`keywords-system-log_images` is truthy, any images that get
inserted into the document are also dumped individually to a file. The name of
the images is based on the name of the log file (via
:ref:`keywords-system-log_images`), or the name of the document if file logging
is disabled. The figure, table or string :ref:`ID <configuration-idc-names>` is
appended after an underscore, and the appropriate extension is added at the
end.

Image logging is implemented individually for tags that generate content. It is
currently supported for the following tags: :ref:`xml-spec-tags-figure`,
:ref:`xml-spec-tags-latex`, :ref:`xml-spec-tags-string` and ocassionally for
:ref:`xml-spec-tags-table`. The strings create small ``.txt`` files containing
the snippets they generate. Custom tags are expected to respect image logging in
a way that makes sense.

Under normal circumstances, the :ref:`tag descriptor <tag-api-descriptors>` is
responsible for logging images. However, in certain cases, the logging can be
done by the content :ref:`handler <plugins-handlers>`. Among the built-in tags,
this is true for :ref:`tables <plugins-tables>`, since the variety of input
data makes it pointless to generalize the type of logging required (as it is
for :ref:`plugins-figures` and :ref:`plugins-strings`).


.. _logging-tags:

-----------------
Logging From Tags
-----------------

The :doc:`tag_api` allows users to process custom tags by implementing a
:py:class:`~imprint.core.tags.TagDescriptor`. Tags should use the
:ref:`engine core's <introduction-layers-engine>` logging facility, provided by
the :py:meth:`~imprint.core.state.EngineState.log` method of the
:py:class:`~imprint.core.state.EngineState`. The reason for using the provided
``log`` method instead of the local logger is that it will attach information
about the parser's position in the XML file to every record.


.. _logging-plugins:

--------------------
Logging From Plugins
--------------------

Unlike :ref:`tag descriptors <tag-api-descriptors>`,
:ref:`plugin handlers <plugins-handlers>` are left to their own devices when it
comes to logging. All of the XML location information will be available from
the surrounding log records provided by the tag, so no real advantage is to be
gained from providing location information. On the other hand, plugins can
access the convenience methods provided by Python's
:doc:`logging framework <library/logging>`, such as
:py:meth:`~logging.Logger.debug` and :py:meth:`~logging.Logger.exception`.

The standard procedure for the :ref:`plugins-builtin` is to get a "private"
modue-level logger, and use that throughout::

    _logger = logging.getLogger(__name__)


.. _logging-levels:

------
Levels
------

In addition to the normal :ref:`logging levels <levels>` provided by the Python
:py:mod:`logging` framework, Imprint sets up the following additional levels:

``TRACE``
    Used to report on the normal activity of a tag processor or plugin that may
    be irrelevant for any but the most fine-grained debugging. The priority
    defaults to 5, which is lower than ``logging.DEBUG`` but higher than
    ``logging.NOTSET``. 
``XTRACE``
    Similar to ``TRACE``, but includes the current exception information by
    default. The priority defaults to 2, which is below that of ``TRACE``. 

All levels are registered with the :py:mod:`logging` framework as if they were
built-in. The appropriate methods are registered with the currently configured
default logger class.
