from sympy import symbols, latex, integrate, simplify

def type2(a, phi, psi, mu, f):
    x, t, xi, tau = symbols('x t xi tau')

    nu1_I1 = simplify((phi.subs(x, x+a*t)+phi.subs(x, x-a*t))/2)
    nu1_I2 = simplify(1/(2*a)*integrate(psi.subs(x, xi), (xi, x-a*t,x+a*t)))
    nu1_I3 = simplify(1/(2*a)*integrate(integrate(f.subs({x: xi, t: tau}), (xi, x-a*(t-tau),x+a*(t-tau))), (tau, 0, t)))
    nu1 = simplify(nu1_I1 + nu1_I2 + nu1_I3)

    nu2_I1 = simplify((phi.subs(x, x+a*t)+phi.subs(x, a*t-x))/2)
    nu2_I2 = simplify(1/(2*a)*(integrate(psi.subs(x, xi), (xi, 0,x+a*t)) + integrate(psi.subs(x, xi), (xi, t-x/a,t))))
    nu2_I3 = simplify(1/(2*a)*(integrate(integrate(f.subs({x: xi, t: tau}), (xi, x-a*(t-tau),x+a*(t-tau))), (tau, t-x/a, t)) + 
                               integrate((
                                    integrate(f.subs({x: xi, t: tau}), (xi, 0,x+a*(t-tau))) +
                                    integrate(f.subs({x: xi, t: tau}), (xi, 0,a*(t-tau) - x))
                               ), (tau, 0, t-x/a))
                               ))
    nu2 = simplify(nu2_I1 + nu2_I2 + nu2_I3)

    omega = simplify(-1*a*integrate(mu.subs(t, tau), (tau, 0, t-x/a)))
    equation = fr"""
    \begin{{align}}
    \text{{Умова задачі}}
    \end{{align}}
    \begin{{cases}}
        u_{{tt}}(x, t) &= {latex(a**2)} u_{{xx}}(x, t) + {latex(f)}, \\
        u(x, 0) &= {latex(phi)}, \ u_t(x, 0) = {latex(psi)}, \\
        2.\ u_x(0, t) &= {latex(mu)}.
    \end{{cases}}
    
    
    \begin{{align}}
    \text{{I. Неоднорідне диференціальне рівняння}}
    \end{{align}}
    \begin{{cases}}
        \nu_{{tt}}(x, t) &= {latex(a**2)} \nu_{{xx}}(x, t) + {latex(f)}, \\
        \nu(x, 0) &= {latex(phi)}, \ \nu_t(x, 0) = {latex(psi)}, \\
        2. \ \nu_x(0, t) &= 0.
    \end{{cases}}

    \begin{{align}}
        \text{{При}}\ t < \frac{{x}}{{{latex(a)}}}, \ x > 0 \\
    \end{{align}}
    \begin{{align}}
    I_1 &= {latex(nu1_I1)} \\
    I_2 &= {latex(nu1_I2)} \\
    I_3 &= {latex(nu1_I3)} \\
    \nu &= {latex(nu1)} \\
    \end{{align}}

    \begin{{align}}
        \text{{При}}\ t > \frac{{x}}{{{latex(a)}}}, \ x > 0
    \end{{align}}
    \begin{{align}}
    I_1 &= {latex(nu2_I1)} \\
    I_2 &= {latex(nu2_I2)} \\
    I_3 &= {latex(nu2_I3)} \\
    \nu &= {latex(nu2)} \\
    \end{{align}}

    \begin{{align}}
    \text{{II. Однорідне диференціальне рівняння}}
    \end{{align}}
    \begin{{cases}}
        \omega_{{tt}}(x, t) &= {latex(a**2)} \omega_{{xx}}(x, t), \\
        \omega(x, 0) &= \omega_t(x, 0) = 0, \\
        2. \ \omega_x(0, t) &= {latex(mu)}. 
    \end{{cases}}

    \begin{{align}}
    \omega(x, t) &=
    \begin{{cases}}
        0, & 0 \leqslant t \leqslant \frac{{x}}{{{latex(a)}}}, \\
        {latex(omega)}, & t > \frac{{x}}{{{latex(a)}}}.
    \end{{cases}}
    \end{{align}}

    \begin{{align}}
    \text{{Відповідь}}
    \end{{align}}
    \begin{{align}}
        &\text{{Якщо }} t < \frac{{x}}{{{latex(a)}}}, \ \text{{то }} u(x,t) = {latex(nu1)} \\
        &\text{{Якщо }} t > \frac{{x}}{{{latex(a)}}}, \ \text{{то }} u(x,t) = {latex(simplify(nu2 + omega))}
    \end{{align}}
    """

    return equation
