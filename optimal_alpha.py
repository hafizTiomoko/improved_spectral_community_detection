def optimal_alpha(qEst,n):
    import numpy as np

    alpha = np.arange(0, 1, 0.01)
    limit = []
    for a in alpha:
        left = 0.0
        right = 100.0

        found_a_valid_point = 0

        e2savetmp = 0
        e2save = 1
        val_external_watchdog = 1000
        external_watchdog = 1

        q_pow_1m2a = np.power(qEst, (1 - 2 * a))
        q_pow_2m2a = np.power(qEst, (2 - 2 * a))

        while (abs(e2savetmp - e2save) > 1e-5 and external_watchdog < val_external_watchdog):
            x = (left + right) / 2
            watchdog = 1
            e2tmp = 0
            e1tmp = 0
            e1 = 1
            e2 = 1

            while (max([abs(e2tmp - e2), abs(e1tmp - e1)]) > 1e-10 and watchdog < 1e2):
                e1tmp = e1
                e2tmp= e2

                den=(1./n)/(-x - q_pow_1m2a * e1tmp + q_pow_2m2a * e2tmp)
                e1 = np.dot(np.squeeze(np.asarray(q_pow_1m2a)),np.squeeze(np.asarray(den)))

                e2 = np.dot(np.squeeze(np.asarray(q_pow_2m2a)),np.squeeze(np.asarray(den)))

                watchdog = watchdog + 1

            if (watchdog < 1e2):
                found_a_valid_point = 1
                e2savetmp = e2save
                right = x
                e2save = e2
            else:
                if (found_a_valid_point == 0):
                    right = 2 * right
                left = x
            external_watchdog += 1

        e2 = e2save

        limit.append(-1.0 / e2)


    # plot(alpha,limit)
    min_value = min(limit)
    index = np.where(limit == min_value)[0]
    alpha = alpha[index]

    return alpha