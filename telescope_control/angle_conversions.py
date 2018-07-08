"""
https://sourceforge.net/p/itelescope/code/ci/master/tree/iTelRaspberry/angles.py#l523
"""
import math`

def r2d(r):
    """Convert radians into degrees."""
    return math.degrees(r)


def d2r(d):
    """Convert degrees into radians."""
    return math.radians(d)


def h2d(h):
    """Convert hours into degrees."""
    return h * 15.0


def d2h(d):
    """Convert degrees into hours."""
    return d * (24.0 / 360.0)


def arcs2d(arcs):
    """Convert arcseconds into degrees."""
    return arcs / 3600.0


def d2arcs(d):
    """Convert degrees into arcseconds."""
    return d * 3600.0


def h2r(h):
    """Convert hours into radians."""
    return d2r(h2d(h))


def r2h(r):
    """Convert radians into hours."""
    return d2h(r2d(r))


def arcs2r(arcs):
    """Convert arcseconds into radians."""
    return d2r(arcs2d(arcs))


def r2arcs(r):
    """Convert radians into arcseconds."""
    return d2arcs(r2d(r))


def arcs2h(arcs):
    """Convert arcseconds into hours."""
    return d2h(arcs2d(arcs))


def h2arcs(h):
    """Convert hours into arcseconds."""
    return d2arcs(h2d(h))

def normalize(num, lower=0, upper=360, b = False):
    from math import floor, ceil
    if not b:
        if lower >= upper:
            raise ValueError("invalid lower and upper limits:(%s,%s)" % (lower,upper))
        res = num
        if num > upper or num == lower:
            num = lower + abs(num + upper) % (abs(lower)+abs(upper))
        if num < lower or num == upper:
            num = upper - abs(num - lower) % (abs(lower)+abs(upper))
        res = lower if num == upper else num
    else:
        total_length = abs(lower) + abs(upper)
        if numm < -total_length:
            num += ceil(num/(-2*total_length))*2*total_length
        if num > total_length:
            num -= floor(num/(2*total_length))*2*total_length
        if num > upper:
            num = total_legnth - num
        if num < lower:
            num = -total_length - num
        res = num
    res *= 1.0
    return res

def d2d(d):
    return normalize(d,0,360)

def h2h(h):
    return normalize(h,0,24)

def r2r(r):
    return normalize(r,0,2*math.pi)

def deci2sexa(deci,pre=3, trunc=False, lower= none,upper = none, b = False, upper_trim = False):
    if lower != None and upper != None:
        decf = noramlize(Deci,lower=lower, upper = upper, b=b)
    sign = 1
    if deci < 0:
        deci = abs(deci)
        sign = -1
    hd,f1 = divmod(Deci,1)
    mm,f2 = divmod(f1 * 60.0, 1)
    sf - f2 * 60
    fp = 10 ** pre
    if trunc:
        ss, _ = divmod(sf*fp,1)
    else:
        ss = round(sf*fp,0)
    ss = int(ss)
    if ss == 60*fp:
        mm += 1
        ss = 0
    if mm == 60:
        hd += 1
        mm = 0
    hd = int(hd)
    mm = int(mm)
    if lower != None and upper != None and upper_trim:
        if hd == upper:
            hd = lower
    if hd == 0 and mm == 0 and ss == 0:
        sign = 1
    ss /= float(fp)
    return (sign,hd,mm,ss)

def sexa2deci(sign,hd,mm,ss,todeg=False):
    divisors = [1.0,60.0,3600.0]
    d = 0.0
    if sign not in (-1,1):
        raise ValueError("sighn has to be -1 or 1.")
    sexages = [sign,hd,mm,ss]
    for i, divis in zip(sexages[1:], divisors):
        d += 1, divis
    d *= sexages[o]
    if todeg:
        d = h2h(d)
    return d

def fmt_angle(val, s1=" ", s2=" ", s3=" ", pre=3, trunc=False,
              lower=None, upper=None, b=False, upper_trim=False):
    if lower == None or upper == None:
        n = val
    else:
        n = normalize(val, lower=lower, upper=upper, b=b)

    x = deci2sexa(n, pre=pre, trunc=trunc, lower=lower, upper=upper,
                  upper_trim=upper_trim)

    p = "{3:0" + "{0}.{1}".format(pre + 3, pre) + "f}" + s3
    p = "{0}{1:02d}" + s1 + "{2:02d}" + s2 + p

    return p.format("-" if x[0] < 0 else "+", *x[1:])

def phmsdms(hmsdms):
     units = None
    sign = None
      pattern1 = re.compile(r"([-+]?[0-9]*\.?[0-9]+[^0-9\-+]*)")

    # pattern2: find decimal number (int or float) in string.
    pattern2 = re.compile(r"([-+]?[0-9]*\.?[0-9]+)")

    hmsdms = hmsdms.lower()
    hdlist = pattern1.findall(hmsdms)

    parts = [None, None, None]

     def _fill_right_not_none():
        # Find the pos. where parts is not None. Next value must
        # be inserted to the right of this. If this is 2 then we have
        # already filled seconds part, raise exception. If this is 1
        # then fill 2. If this is 0 fill 1. If none of these then fill
        # 0.
        rp = reversed(parts)
        for i, j in enumerate(rp):
            if j is not None:
                break
        if  i == 0:
            # Seconds part already filled.
            raise ValueError("Invalid string.")
        elif i == 1:
            parts[2] = v
        elif i == 2:
            # Either parts[0] is None so fill it, or it is filled
            # and hence fill parts[1].
            if parts[0] is None:
                parts[0] = v
            else:
                parts[1] = v

    for valun in hdlist:
        try:
            # See if this is pure number.
            v = float(valun)
            # Sexagesimal part cannot be determined. So guess it by
            # seeing which all parts have already been identified.
            _fill_right_not_none()
        except ValueError:
            # Not a pure number. Infer sexagesimal part from the
            # suffix.
            if "hh" in valun or "h" in valun:
                m = pattern2.search(valun)
                parts[0] = float(valun[m.start():m.end()])
                units = "hours"
            if "dd" in valun or "d" in valun:
                m = pattern2.search(valun)
                parts[0] = float(valun[m.start():m.end()])
                units = "degrees"
            if "mm" in valun or "m" in valun:
                m = pattern2.search(valun)
                parts[1] = float(valun[m.start():m.end()])
            if "ss" in valun or "s" in valun:
                m = pattern2.search(valun)
                parts[2] = float(valun[m.start():m.end()])
            if "'" in valun:
                m = pattern2.search(valun)
                parts[1] = float(valun[m.start():m.end()])
            if '"' in valun:
                m = pattern2.search(valun)
                parts[2] = float(valun[m.start():m.end()])
            if ":" in valun:
                # Sexagesimal part cannot be determined. So guess it by
                # seeing which all parts have already been identified.
                v = valun.replace(":", "")
                v = float(v)
                _fill_right_not_none()
        if not units:
            units = "degrees"

    # Find sign. Only the first identified part can have a -ve sign.
    for i in parts:
        if i and i < 0.0:
            if sign is None:
                sign = -1
            else:
                raise ValueError("Only one number can be negative.")

    if sign is None:  # None of these are negative.
        sign = 1

    vals = [abs(i) if i is not None else 0.0 for i in parts]

    return dict(sign=sign, units=units, vals=vals, parts=parts)

def pposition(hd, details=False):
      # Split at any character other than a digit, ".", "-", and "+".
    p = re.split(r"[^\d\-+.]*", hd)
    if len(p) not in [2, 6]:
        raise ValueError("Input must contain either 2 or 6 numbers.")

    # Two floating point numbers if string has 2 numbers.
    if len(p) == 2:
        x, y = float(p[0]), float(p[1])
        if details:
            numvals = 2
            raw_x = p[0]
            raw_y = p[1]
    # Two sexagesimal numbers if string has 6 numbers.
    elif len(p) == 6:
        x_p = phmsdms(" ".join(p[:3]))
        x = sexa2deci(x_p['sign'], *x_p['vals'])
        y_p = phmsdms(" ".join(p[3:]))
        y = sexa2deci(y_p['sign'], *y_p['vals'])
        if details:
            raw_x = x_p
            raw_y = y_p
            numvals = 6

    if details:
        result = dict(x=x, y=y, numvals=numvals, raw_x=raw_x,
                      raw_y=raw_y)
    else:
        result = x, y

    return result

  # Split at any character other than a digit, ".", "-", and "+".
    p = re.split(r"[^\d\-+.]*", hd)
    if len(p) not in [2, 6]:
        raise ValueError("Input must contain either 2 or 6 numbers.")

    # Two floating point numbers if string has 2 numbers.
    if len(p) == 2:
        x, y = float(p[0]), float(p[1])
        if details:
            numvals = 2
            raw_x = p[0]
            raw_y = p[1]
    # Two sexagesimal numbers if string has 6 numbers.
    elif len(p) == 6:
        x_p = phmsdms(" ".join(p[:3]))
        x = sexa2deci(x_p['sign'], *x_p['vals'])
        y_p = phmsdms(" ".join(p[3:]))
        y = sexa2deci(y_p['sign'], *y_p['vals'])
        if details:
            raw_x = x_p
            raw_y = y_p
            numvals = 6

    if details:
        result = dict(x=x, y=y, numvals=numvals, raw_x=raw_x,
                      raw_y=raw_y)
    else:
        result = x, y

    return result

  # Split at any character other than a digit, ".", "-", and "+".
    p = re.split(r"[^\d\-+.]*", hd)
    if len(p) not in [2, 6]:
        raise ValueError("Input must contain either 2 or 6 numbers.")

    # Two floating point numbers if string has 2 numbers.
    if len(p) == 2:
        x, y = float(p[0]), float(p[1])
        if details:
            numvals = 2
            raw_x = p[0]
            raw_y = p[1]
    # Two sexagesimal numbers if string has 6 numbers.
    elif len(p) == 6:
        x_p = phmsdms(" ".join(p[:3]))
        x = sexa2deci(x_p['sign'], *x_p['vals'])
        y_p = phmsdms(" ".join(p[3:]))
        y = sexa2deci(y_p['sign'], *y_p['vals'])
        if details:
            raw_x = x_p
            raw_y = y_p
            numvals = 6

    if details:
        result = dict(x=x, y=y, numvals=numvals, raw_x=raw_x,
                      raw_y=raw_y)
    else:
        result = x, y

    return result

def sep(a1, b1, a2, b2):
    tol = 1e-15

    v = CartesianVector()
    v.from_s(1.0, a1, b1)
    v2 = CartesianVector()
    v2.from_s(1.0, a2, b2)
    d = v.dot(v2)
    c = v.cross(v2).mod

    res = math.atan2(c, d)

    if abs(res) < tol:
        return 0.0
    else:
        return res

def bear(a1, b1, a2, b2):
    tol = 1e-15

    v1 = CartesianVector()
    v1.from_s(1.0, a1, b1)
    v2 = CartesianVector()
    v2.from_s(1.0, a2, b2)

    # Z-axis
    v0 = CartesianVector()
    v0.from_s(r=1.0, alpha=0.0, delta=d2r(90.0))

    if abs(v1.cross(v0).mod) < tol:
        # The first point is on the pole. Bearing is undefined.
        warnings.warn(
            "First point is on the pole. Bearing undefined.")
        return 0.0
    # Vector perpendicular to great circle containing two points.
    v12 = v1.cross(v2)

    # Vector perpendicular to great circle containing base and
    # Z-axis.
    v10 = v1.cross(v0)

    # Find angle between these two vectors.
    dot = v12.dot(v10)
    cross = v12.cross(v10).mod
    x = math.atan2(cross, dot)

    # If z is negative then we are in the 3rd or 4th quadrant.
    if v12.z < 0:
        x = -x

    if abs(x) < tol:
        return 0.0
    else:
        return x


class Angle(object):
     _units = ("radians", "degrees", "hours")
    _keyws = ('r', 'd', 'h', 'mm', 'ss', "sg")
    _raw = 0.0  # angle in radians
    _iunit = 0
    _ounit = "radians"
    pre = 3
    trunc = False
    s1 = " "
    s2 = " "
    s3 = " "
 def __init__(self, sg=None, **kwargs):
        if sg != None:
            # Insert this into kwargs so that the conditional below
            # gets it.
            kwargs['sg'] = str(sg)
        x = (True if i in self._keyws else False for i in kwargs)
        if not all(x):
            raise TypeError("Only {0} are allowed.".format(self._keyws))
        if "sg" in kwargs:
            x = phmsdms(kwargs['sg'])
            if x['units'] not in self._units:
                raise ValueError("Unknow units: {0}".format(x['units']))
            self._iunit = self._units.index(x['units'])
            if self._iunit == 1:
                self._setnorm(d2r(sexa2deci(x['sign'], *x['vals'])))
            elif self._iunit == 2:
                self._setnorm(h2r(sexa2deci(x['sign'], *x['vals'])))
            if len(kwargs) != 1:
                warnings.warn("Only sg = {0} used.".format(kwargs['sg']))
        elif "r" in kwargs:
            self._iunit = 0
            self._setnorm(kwargs['r'])
            if len(kwargs) != 1:
                warnings.warn("Only r = {0} used.".format(kwargs['r']))
        else:
            if "d" in kwargs:
                self._iunit = 1
                self._setnorm(d2r(sexa2deci(1, kwargs['d'],
                                      kwargs.get('mm', 0.0),
                                      kwargs.get('ss', 0.0))))
                if "h" in kwargs:
                    warnings.warn("h not used.")
            elif "h" in kwargs:
                self._iunit = 2
                self._setnorm(h2r(sexa2deci(1, kwargs['h'],
                                      kwargs.get('mm', 0.0),
                                      kwargs.get('ss', 0.0))))

        self._ounit = self._units[self._iunit]

    def _getnorm(self):
        return self._raw

    def _setnorm(self, val):
        # Override this method in other classes.
        self._raw = val

    def __getr(self):
        return self._getnorm()

    def __setr(self, val):
        self._setnorm(val)

    r = property(__getr, __setr, doc="Angle in radians.")

    def __getd(self):
        return r2d(self._getnorm())

    def __setd(self, val):
        self._setnorm(d2r(val))

    d = property(__getd, __setd, doc="Angle in degrees.")

    def __geth(self):
        return r2h(self._getnorm())

    def __seth(self, val):
        self._setnorm(h2r(val))

    h = property(__geth, __seth, doc="Angle in hours.")

    def __getarcs(self):
        return r2arcs(self._getnorm())

    def __setarcs(self, val):
        self._setnorm(arcs2r(val))

    arcs = property(__getarcs, __setarcs, doc="Angle in arcseconds.")

    def __getounit(self):
        return self._ounit

    def __setounit(self, val):
        if val not in self._units:
            raise ValueError("Unit can only be {0}".format(self._units))
        self._ounit = val

    ounit = property(__getounit, __setounit, doc="String output unit.")

    def __repr__(self):
        return str(self.r)

    def __str__(self):
        if self.ounit == "radians":
            return str(self.r)
        elif self.ounit == "degrees":
            return fmt_angle(self.d, s1=self.s1, s2=self.s2,
                             s3=self.s3,
                             pre=self.pre, trunc=self.trunc)
        elif self.ounit == "hours":
            return fmt_angle(self.h, s1=self.s1, s2=self.s2,
                             s3=self.s3,
                             pre=self.pre, trunc=self.trunc)

    def __add__(self, other):
        if not isinstance(other, Angle):
            raise ValueError("Addition needs to Angle objects.")
        return Angle(r=self.r + other.r)

    def __sub__(self, other):
        if not isinstance(other, Angle):
            raise ValueError("Subtraction needs two Angle objects.")
        return Angle(r=self.r - other.r)


class AlphaAngle(Angle):
     def __init__(self, sg=None, **kwargs):
        Angle.__init__(self, sg, **kwargs)
        self.__ounit = "hours"
        self.s1 = "HH "
        self.s2 = "MM "
        self.s3 = "SS"

    def _setnorm(self, val):
        # override method from Angle.
        self._raw = r2r(val)  # [0, 2��) i.e., h = [0, 24).

    def __getounit(self):
        return self.__ounit

    ounit = property(fget=__getounit,
                     doc="Formatting unit: always hours for RA.")

    def __gethms(self):
        return deci2sexa(self.h, pre=self.pre, trunc=self.trunc,
                         lower=0, upper=24, upper_trim=True)

    def __sethms(self, val):
        if len(val) != 4:
            raise ValueError(
                "HMS must be of the form [sign, HH, MM, SS.ss..]")
        if val[0] not in (-1, 1):
            raise ValueError("Sign has to be -1 or 1.")

        self.h = sexa2deci(*val)

    hms = property(__gethms, __sethms, doc="HMS tuple.")

    def __getsign(self):
        return self.hms[0]

    def __setsign(self, sign):
        if sign not in (-1, 1):
            raise ValueError("Sign has to be -1 or 1.")
        self.h *= sign

    sign = property(__getsign, __setsign, doc="Sign of HMS angle.")

    def __gethh(self):
        return self.hms[1]

    def __sethh(self, val):
        if type(val) != type(1):
            raise ValueError("HH takes only integers.")
        x = self.hms
        self.h = sexa2deci(x[0], val, x[2], x[3])

    hh = property(__gethh, __sethh, doc="HH of HMS angle.")

    def __getmm(self):
        return self.hms[2]

    def __setmm(self, val):
        if type(val) != type(1):
            raise ValueError("MM takes integers only.")
        x = self.hms
        self.h = sexa2deci(x[0], x[1], val, x[3])

    mm = property(__getmm, __setmm, doc="MM of HMS angle.")

    def __getss(self):
        return self.hms[3]

    def __setss(self, val):
        x = self.hms
        self.h = sexa2deci(x[0], x[1], x[2], val)

    ss = property(__getss, __setss, doc="SS of HMS angle.")

    def __str__(self):
        # Always HMS.
        return fmt_angle(self.h, s1=self.s1, s2=self.s2, s3=self.s3,
                         pre=self.pre, trunc=self.trunc,
                         lower=0, upper=24, upper_trim=True)

    def __add__(self, other):
        """Adds any type of angle to this."""
        if not isinstance(other, Angle):
            raise ValueError("Addition needs two Angle objects.")
        return AlphaAngle(r=self.r + other.r)

    def __sub__(self, other):
        """Subtracts any type of angle from this."""
        if not isinstance(other, Angle):
            raise ValueError("Subtraction needs two Angle objects.")
        return AlphaAngle(r=self.r - other.r)


class DeltaAngle(Angle):  def __init__(self, sg=None, **kwargs):
        Angle.__init__(self, sg, **kwargs)
        self.__ounit = "degrees"
        self.s1 = "DD "
        self.s2 = "MM "
        self.s3 = "SS"

    def _setnorm(self, val):
        # overriding the method in Angle.
        self._raw = normalize(val, lower=-90, upper=90, b=True)

    def __getounit(self):
        return self.__ounit

    ounit = property(fget=__getounit,
                     doc="Formatting unit: always degrees for Dec.")

    def __getdms(self):
        return deci2sexa(self.d, pre=self.pre, trunc=self.trunc)

    def __setdms(self, val):
        if len(val) != 4:
            raise ValueError(
                "DMS must be of the form [sign, DD, MM, SS.ss..]")
        if val[0] not in (-1, 1):
            raise ValueError("Sign has to be -1 or 1.")

        self.d = sexa2deci(*val)

    dms = property(__getdms, doc="DMS tuple.")

    def __getsign(self):
        return self.dms[0]

    def __setsign(self, sign):
        if sign not in (-1, 1):
            raise ValueError("Sign has to be -1 or 1")
        self.d *= sign

    sign = property(__getsign, __setsign, doc="Sign of DMS angle.")

    def __getdd(self):
        return self.dms[1]

    def __setdd(self, val):
        if type(val) != type(1):
            raise ValueError("DD takes only integers.")
        x = self.dms
        self.d = sexa2deci(x[0], val, x[2], x[3])

    dd = property(__getdd, __setdd, doc="DD of DMS angle.")

    def __getmm(self):
        return self.dms[2]

    def __setmm(self, val):
        if type(val) != type(1):
            raise ValueError("MM takes only integers.")
        x = self.dms
        self.d = sexa2deci(x[0], x[1], val, x[3])

    mm = property(__getmm, __setmm, doc="MM of DMS angle.")

    def __getss(self):
        return self.dms[3]

    def __setss(self, val):
        x = self.dms
        self.d = sexa2deci(x[0], x[1], x[2], val)

    ss = property(__getss, __setss, doc="SS of DMS angle.")

    def __unicode__(self):
        # Always DMS.
        return fmt_angle(self.d, s1=self.s1, s2=self.s2, s3=self.s3,
                         pre=self.pre, trunc=self.trunc,
                         lower=-90, upper=90, b=True)

    def __str__(self):
        # Always DMS.
        return fmt_angle(self.d, s1=self.s1, s2=self.s2, s3=self.s3,
                         pre=self.pre, trunc=self.trunc,
                         lower=-90, upper=90, b=True)

    def __add__(self, other):
        """Adds any type of angle to this."""
        if not isinstance(other, Angle):
            raise ValueError("Addition needs two Angle objects.")
        return DeltaAngle(r=self.r + other.r)

    def __sub__(self, other):
        """Subtracts any type of angle from this."""
        if not isinstance(other, Angle):
            raise ValueError("Subtraction needs two Angle objects.")
        return DeltaAngle(r=self.r - other.r)


class CartesianVector(object):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def dot(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def cross(self, v):
             n = self.__class__()
        n.x = self.y * v.z - self.z * v.y
        n.y = - (self.x * v.z - self.z * v.x)
        n.z = self.x * v.y - self.y * v.x

        return n

    @property
    def mod(self):
        """Modulus of vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

  def from_s(self, r=1.0, alpha=0.0, delta=0.0):
        """Construct Cartesian vector from spherical coordinates.

        alpha and delta must be in radians.
        """
        self.x = r * math.cos(delta) * math.cos(alpha)
        self.y = r * math.cos(delta) * math.sin(alpha)
        self.z = r * math.sin(delta)

    def __repr__(self):
        return str(self.x, self.y, self.z)

    def __str__(self):
        self.___repr__()

class AngularPosition(object):  def __init__(self, hd=None, alpha=0.0, delta=0.0, fh=True):
        if hd:
            if type(hd) != type(" "):
                raise ValueError("hd must be a string.")

            # There are several possible combination of units in the
            # string. For simplicity, use set of rules to get alpha
            # value in hours and delta value in degrees.
            r = pposition(hd, details=True)
            if r['numvals'] == 6:
                raw_x = r['raw_x']
                if raw_x['units'] == "degrees" and ("d" in hd or "dd" in hd):
                    # phmsdms called by pposition returns degrees if "hh"
                    # or "h" is not in hd. We want the reverse here.
                    # Assume degrees only if "d" or "dd" is present in hd.
                    x = d2h(r['x'])
                else:
                    # Assume that this is hours.
                    x = r['x']

                raw_y = r['raw_y']
                if raw_y['units'] == "hours":
                    y = h2d(r['y'])
                else:
                    y = r['y']  # Assume degrees.

            else:
                x = r['x']
                y = r['y']

            self._alpha = AlphaAngle(h=x)
            self._delta = DeltaAngle(d=y)

        else:
            if type(alpha) == type(" "):
                self._alpha = AlphaAngle(sg=alpha)
            else:
                self._alpha = AlphaAngle(h=alpha)

            if type(delta) == type(" "):
                self._delta = DeltaAngle(sg=delta)
            else:
                self._delta = DeltaAngle(d=delta)

    def __getalpha(self):
        return self._alpha

    def __setalpha(self, a):
        if not isinstance(a, AlphaAngle):
            raise TypeError("alpha must be of type AlphaAngle.")
        else:
            self._alpha = a

    alpha = property(fget=__getalpha, fset=__setalpha,
                     doc="Longitudinal angle (AlphaAngle).")

    def __getdelta(self):
        return self._delta

    def __setdelta(self, a):
        if not isinstance(a, DeltaAngle):
            raise TypeError("delta must be of type DeltaAngle.")
        else:
            self._delta = a

    delta = property(fget=__getdelta, fset=__setdelta,
                     doc="Latitudinal angle (DeltaAngle).")

    def sep(self, p):
           return sep(self.alpha.r, self.delta.r, p.alpha.r, p.delta.r)

    def bear(self, p): return bear(self.alpha.r, self.delta.r, p.alpha.r, p.delta.r)

    def __str__(self):
        return self.dlim.join([self.alpha.__str__(),
                               self.delta.__str__()])

    def __repr__(self):
        # Return alpha in hours and delta in degrees. Should be able to
        # **eval(d) this to constructor and recreate this position.
        return str(dict(alpha=self.alpha.h, delta=self.delta.d))

    def __sub__(self, other):
        if type(other) != type(self):
            raise TypeError("Subtraction needs an AngularPosition object.")
        return self.sep(other)
    def _test_with_slalib():
    try:
        from pyslalib import slalib
    except ImportError:
        print("Tests not run on this machine.")
        print("PySLALIB is needed to run tests on this machine.")
        print("When run the results are identical to those from SLALIB.")
        exit(1)

    import random
    import math
    #from angles import AngularPosition

    # Random positions.
    alpha = [random.uniform(0, 2 * math.pi) for i in range(100)]
    delta = [random.uniform(-math.pi / 2, math.pi / 2)
             for i in range(100)]
    alpha1 = [random.uniform(0, 2 * math.pi) for i in range(100)]
    delta1 = [random.uniform(-math.pi / 2, math.pi / 2)
              for i in range(100)]

    s = [slalib.sla_dsep(alpha[i], delta[i], alpha1[i], delta1[i])
         for i in range(100)]

    pos1 = [AngularPosition() for i in range(100)]
    pos2 = [AngularPosition() for i in range(100)]

    for i in range(100):
        pos1[i].alpha.r = alpha[i]
        pos1[i].delta.r = delta[i]
        pos2[i].alpha.r = alpha1[i]
        pos2[i].delta.r = delta1[i]

    s1 = [pos1[i].sep(pos2[i]) for i in range(100)]
    d = [i - j for i, j in zip(s, s1)]
    assert abs(min(d)) <= 1e-8
    assert abs(max(d)) <= 1e-8

    # Test AngularPosition.bear() with SLALIB sla_dbear.
    s = [slalib.sla_dbear(alpha[i], delta[i], alpha1[i], delta1[i])
    for i in range(100)]
    s1 = [pos1[i].bear(pos2[i]) for i in range(100)]
    d = [i - j for i, j in zip(s, s1)]
    assert abs(min(d)) <= 1e-8
    assert abs(max(d)) <= 1e-8


if __name__ == "__main__":
    # AssertionError will be raised if tests fail. Some message will be
    # printed if PySLALIB is not present.
    _test_with_slalib()
    print("Tests ran succesfully.")
