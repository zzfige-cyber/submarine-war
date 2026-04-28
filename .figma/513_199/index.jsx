import React from 'react';

import styles from './index.module.scss';

const Component = () => {
  return (
    <div className={styles.frame}>
      <div className={styles.vector24}>
        <p className={styles.text3}>
          <span className={styles.text}>「空格」</span>
          <span className={styles.text2}>投水雷</span>
        </p>
        <p className={styles.text5}>
          <span className={styles.text}>「</span>
          <span className={styles.text4}>←‌ ‌→</span>
          <span className={styles.text}>‌」</span>
          <span className={styles.text2}>移动</span>
        </p>
        <img src="../image/moh5gwvv-5as36al.svg" className={styles.group43} />
      </div>
    </div>
  );
}

export default Component;
