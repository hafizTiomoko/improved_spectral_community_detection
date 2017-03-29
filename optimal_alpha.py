def optimal_alpha(qEst,n):
    import numpy as np

    alpha = np.arange(0, 1, 0.01)
    limit = []
    for a in alpha:
        left = 0.0
        right = 100.0

        found_a_valid_point = 0

        gsavetmp = 0
        gsave = 1
        val_external_watchdog = 1000
        external_watchdog = 1

        q_pow_1m2a = np.power(qEst, (1 - 2 * a))
        q_pow_2m2a = np.power(qEst, (2 - 2 * a))

        while (abs(gsavetmp - gsave) > 1e-5 and external_watchdog < val_external_watchdog):
            x = (left + right) / 2
            watchdog = 1
            ftmp = 0
            gtmp = 0
            f = 1
            g = 1

            while (max([abs(gtmp - g), abs(ftmp - f)]) > 1e-10 and watchdog < 1e2):
                ftmp = f
                gtmp= g

                den=(1./n)/(-x - q_pow_1m2a * ftmp + q_pow_2m2a * gtmp)
                f = np.dot(np.squeeze(np.asarray(q_pow_1m2a)),np.squeeze(np.asarray(den)))

                g = np.dot(np.squeeze(np.asarray(q_pow_2m2a)),np.squeeze(np.asarray(den)))

                watchdog = watchdog + 1

            if (watchdog < 1e2):
                found_a_valid_point = 1
                gsavetmp = gsave
                right = x
                gsave = g
            else:
                if (found_a_valid_point == 0):
                    right = 2 * right
                left = x
            external_watchdog += 1

        g = gsave

        limit.append(-1.0 / g)


    # plot(alpha,limit)
    min_value = min(limit)
    index = np.where(limit == min_value)[0]
    alpha = alpha[index]

    return alpha
