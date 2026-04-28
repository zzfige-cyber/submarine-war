import React from 'react';

import styles from './index.module.scss';

const Component = () => {
  return (
    <div className={styles.frame}>
      <img src="../image/mohdxzav-rl762us.png" className={styles.rectangle79} />
      <div className={styles.maskGroup2}>
        <div className={styles.group38}>
          <div className={styles.gameover}>
            <div className={styles.rectangle82} />
            <div className={styles.rectangle77} />
            <p className={styles.missionAccomplished3}>
              <span className={styles.missionAccomplished}>
                Mission
                <br />
              </span>
              <span className={styles.missionAccomplished2}>Accomplished</span>
            </p>
          </div>
        </div>
        <img src="../image/mohdxzav-eaeou56.svg" className={styles.maskGroup} />
        <div className={styles.rectangle86}>
          <div className={styles.group58}>
            <div className={styles.rectangle87} />
            <div className={styles.rectangle88} />
            <div className={styles.rectangle89} />
          </div>
          <p className={styles.text}>通关时间</p>
          <div className={styles.group58}>
            <div className={styles.rectangle87} />
            <div className={styles.rectangle88} />
            <div className={styles.rectangle89} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Component;
