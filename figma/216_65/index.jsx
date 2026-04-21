import React from 'react';

import styles from './index.module.scss';

const Component = () => {
  return (
    <div className={styles.frame2}>
      <div className={styles.frame}>
        <div className={styles.autoWrapper3}>
          <div className={styles.autoWrapper}>
            <p className={styles.hP}>HP</p>
            <img
              src="../image/mo7ajtwh-t7s4sfp.svg"
              className={styles.rectangle26}
            />
          </div>
          <div className={styles.autoWrapper2}>
            <p className={styles.hP}>MP</p>
            <img
              src="../image/mo7ajtwh-h152m31.svg"
              className={styles.rectangle26}
            />
          </div>
        </div>
        <img src="../image/mo7ajtwh-bm0ml2j.svg" className={styles.group26} />
        <p className={styles.a1000}>1000</p>
      </div>
    </div>
  );
}

export default Component;
