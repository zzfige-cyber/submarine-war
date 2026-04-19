import React from 'react';

import styles from './index.module.scss';

const Component = () => {
  return (
    <div className={styles.frame}>
      <div className={styles.group14}>
        <div className={styles.autoWrapper}>
          <img src="../image/mo5rajpc-y4175g8.png" className={styles.union} />
          <img src="../image/mo5rajpc-nbf4bip.svg" className={styles.rectangle8} />
          <div className={styles.rectangle7}>
            <p className={styles.text}>移动速度</p>
            <p className={styles.text2}>每升1级+10%的移速</p>
          </div>
          <div className={styles.rectangle9}>
            <p className={styles.text3}>装甲厚度</p>
            <p className={styles.text4}>每升1级+最大血量20%</p>
          </div>
          <div className={styles.rectangle10}>
            <p className={styles.text5}>弹药库</p>
            <p className={styles.text6}>每升1级弹药库容量+20%</p>
          </div>
          <div className={styles.group2}>
            <div className={styles.ellipse4} />
            <div className={styles.ellipse4} />
            <div className={styles.ellipse4} />
          </div>
          <div className={styles.group8}>
            <div className={styles.ellipse4} />
            <div className={styles.ellipse5} />
            <div className={styles.ellipse5} />
          </div>
          <div className={styles.group11}>
            <div className={styles.ellipse4} />
            <div className={styles.ellipse5} />
          </div>
          <p className={styles.text9}>
            <span className={styles.text7}>剩余技能点：</span>
            <span className={styles.text8}>5/5</span>
          </p>
        </div>
        <div className={styles.autoWrapper5}>
          <div className={styles.autoWrapper2}>
            <img src="../image/mo5rajpd-z1eg6og.png" className={styles.group6} />
            <img src="../image/mo5rajpd-wvthd58.png" className={styles.group7} />
          </div>
          <div className={styles.autoWrapper3}>
            <img src="../image/mo5rajpd-z908rvp.png" className={styles.group10} />
            <img src="../image/mo5rajpd-qq9en6s.png" className={styles.group9} />
          </div>
          <div className={styles.autoWrapper4}>
            <img src="../image/mo5rajpd-kbsll61.png" className={styles.group13} />
            <img src="../image/mo5rajpd-kk35uk8.png" className={styles.group12} />
          </div>
        </div>
      </div>
      <p className={styles.skIllcongiguration}>SkILL CONGIGURATION</p>
    </div>
  );
}

export default Component;
