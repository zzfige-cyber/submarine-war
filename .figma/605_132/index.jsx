import React from 'react';

import styles from './index.module.scss';

const Component = () => {
  return (
    <div className={styles.frame}>
      <img src="../image/moiu2v2b-2miscee.png" className={styles.union} />
      <div className={styles.union2}>
        <p className={styles.text}>上传全球排行榜？</p>
      </div>
    </div>
  );
}

export default Component;
